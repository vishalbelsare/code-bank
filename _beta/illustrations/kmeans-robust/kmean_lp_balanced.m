function [clusters_reopt, dist_reopt, lp_obj] = ...
    kmean_lp_balanced(observations, K, n_outliers)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% NOTE: 'K' is supposed to be the number of desired, actual clusters     %
% (i.e. NOT counting the outliers as an additional separate cluster)     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if nargin <= 2
    n_outliers = 0;
end

% extract some problem parameters
N = size(observations, 2);
dim = size(observations, 1);
sizes = (N-n_outliers)/K*ones(1,K);

% check whether balanced clustering is possible
if mod(N-n_outliers,K) ~= 0
    fprintf(' * Balanced clustering is not possible!\n');
    return;
end

% construct distance matrix D
D = zeros(N);
for i = 1:N
for j = 1:N
    D(i,j) = norm(observations(:,i) - observations(:,j))^2;
end
end

% initialize indices to indicate the optimal clusters
clusters_opt = zeros(N,1);

% determine the outliers and mark them with cluster index "-1"
[idx, lp_obj_1] = find_outliers(observations, K, n_outliers);
clusters_opt(idx) = -1;

% determine the first actual cluster
unassigned = find(clusters_opt == 0);
[idx, lp_obj_2] = kmean_sdp_iter(observations(:,unassigned), K);
clusters_opt(unassigned(idx)) = 1;

% choose relaxed distance to return
if n_outliers == 0
    lp_obj = lp_obj_2;
else
    lp_obj = lp_obj_1;
end

% determine the remaining actual clusters
for k = 2:(K-1)
    unassigned = find(clusters_opt == 0);
    idx = kmean_sdp_iter(observations(:,unassigned), K-k+1);
    clusters_opt(unassigned(idx)) = k;
end
clusters_opt(clusters_opt == 0) = K;

%{
* refinement (improve clustering)
* "1" iteration of lloyd algorithm
%}
% determine the center of each cluster
centers = zeros(dim,K);
for k = 1:K %#ok<*FNDSB>
    centers(:,k) = mean(observations(:, find(clusters_opt == k)),2);
end

% drop outliers from the set of observations
idx_cleaned = find(clusters_opt > 0);
observations_cleaned = observations(:,idx_cleaned);
N_cleaned = N - n_outliers;

% distance from each cleaned observation to each center
dist_to_center = zeros(N_cleaned,K); 
for i = 1:N_cleaned
for k = 1:K
    dist_to_center(i,k) = norm(observations_cleaned(:,i) - centers(:,k))^2;
end
end

% set up and solve a linear assignment problem
assg = sdpvar(N_cleaned, K, 'full');
constraints = [assg >= 0, sum(assg) >= sizes, sum(assg,2) == 1];
options = sdpsettings('verbose', 0, 'solver', 'mosek', 'cachesolvers', 1);
optimize(constraints, assg(:)'*dist_to_center(:), options); 

% recover the cleaned clusters from solution of assignment problem
clusters_cleaned_reopt = double(assg);
clusters_cleaned_reopt = clusters_cleaned_reopt.*(ones(N_cleaned,1)*(1:K));
clusters_cleaned_reopt = sum(clusters_cleaned_reopt, 2);
clusters_cleaned_reopt = round(clusters_cleaned_reopt);

% cast the cleaned clusters in terms of the origianl observations
clusters_reopt = clusters_opt;
clusters_reopt(idx_cleaned) = clusters_cleaned_reopt;

% compute distance achieved by this assignment
dist_reopt = 0;
for k = 1:K
    index = find(clusters_reopt == k);
    dist_reopt = dist_reopt + sum(sum(D(index,index)))/2/sizes(k);
end

end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [first_cluster, lp_obj] = ...
    kmean_sdp_iter(observations, K) 

% extract number of observations
N = size(observations, 2); 

% check whether balanced clustering is possible
if mod(N,K) ~= 0
    fprintf(' * Balanced clustering is not possible!\n');
    return;
end

%{
* construct distance matrix D 
%}
D = zeros(N);
for i = 1:N
for j = 1:N
    D(i,j) = norm(observations(:,i) - observations(:,j))^2;
end
end

%{
* construct a (primal) LP
%}

% decision variables
M = sdpvar(N, N);
x = sdpvar(N, 1);
L = sdpvar(N, N);
y = sdpvar(N, 1);

% auxiliary quantities
Mx_1 = M + x*ones(1,N) + ones(N,1)*x' + 1;
Mx_2 = M - x*ones(1,N) - ones(N,1)*x' + 1;
Mx_3 = 1 + x*ones(1,N) - ones(N,1)*x' - M;
Mx_4 = 1 + ones(N,1)*x' - x*ones(1,N) - M;
Ly_1 = L + y*ones(1,N) + ones(N,1)*y' + 1;
Ly_2 = L - y*ones(1,N) - ones(N,1)*y' + 1;
Ly_3 = 1 + y*ones(1,N) - ones(N,1)*y' - L;
Ly_4 = 1 + ones(N,1)*y' - y*ones(1,N) - L;

% set up constraints
constraints = [x(1) == 1, x >= -1, x <= 1, y >= -1, y <= 1];
constraints = [constraints, diag(M) == 1, diag(L) == 1];
constraints = [constraints, sum(M,2) == N*(2/K-1)*x];
constraints = [constraints, sum(L,2) == N*(2/K-1)*y];
constraints = [constraints, sum(x) == N*(2/K-1), sum(y) == N*(2/K-1)];
constraints = [constraints, x + (K-1)*y == 2-K];
constraints = [constraints, Mx_1(:) >= 0, Mx_2(:) >= 0];
constraints = [constraints, Ly_1(:) >= 0, Ly_2(:) >= 0];
constraints = [constraints, Mx_3(:) >= 0, Mx_4(:) >= 0];
constraints = [constraints, Ly_3(:) >= 0, Ly_4(:) >= 0];

% set up objective
obj_x = sum(sum(D.*(ones(N) + M + x*ones(1,N) + ones(N,1)*x')));
obj_y = sum(sum(D.*(ones(N) + L + y*ones(1,N) + ones(N,1)*y')));
obj = (obj_x + (K-1)*obj_y)*K/N/8;

% solve primal LP
options = sdpsettings('verbose', 0, 'solver', 'mosek', 'cachesolvers', 1);
diagnosis = optimize(constraints, obj, options);
% fprintf('%s \n', diagnosis.info);
lp_obj = double(obj);

%{
* Rounding LP solution to retrieve a cluster
%}
x = double(x);
[~, srt] = sort(x, 1, 'descend');
first_cluster = srt(1:(N/K));

end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [outliers, lp_obj] = ...
    find_outliers(observations, K, n_outliers)  %#ok<*DEFNU>

% extract total number of observations and number of observations per cluster
N = size(observations, 2);
n = (N - n_outliers)/K;

%{
* construct distance matrix D 
%}
D = zeros(N);
for i = 1:N
for j = 1:N
    D(i,j) = norm(observations(:,i) - observations(:,j))^2;
end
end

%{
* construct a (primal) SDP
%}

% variables belonging to outliers
%L = sdpvar(N, N);
y = sdpvar(N, 1);

% varialbes belonging to actual clusters
M = sdpvar(N, N);
x = sdpvar(N, 1);

% auxiliary quantities
Mx_1 = M + x*ones(1,N) + ones(N,1)*x' + 1;
Mx_2 = M - x*ones(1,N) - ones(N,1)*x' + 1;
Mx_3 = 1 + x*ones(1,N) - ones(N,1)*x' - M;
Mx_4 = 1 + ones(N,1)*x' - x*ones(1,N) - M;

% set up LP constraints
constraints = [diag(M) == 1, y >= -1, y <= 1, x >= -1, x <= 1];
constraints = [constraints, sum(M,2) == (2*n-N)*x];
constraints = [constraints, sum(x) == 2*n-N];
constraints = [constraints, sum(y) == 2*n_outliers-N];
constraints = [constraints, y + K*x == 1-K];
constraints = [constraints, Mx_1(:) >= 0, Mx_2(:) >= 0];
constraints = [constraints, Mx_3(:) >= 0, Mx_4(:) >= 0];

% set up LP objective
obj = sum(sum(D.*(ones(N) + M + x*ones(1,N) + ones(N,1)*x')))*K/n/8;

% solve primal LP
options = sdpsettings('verbose', 0, 'solver', 'mosek', 'cachesolvers', 1);
diagnosis = optimize(constraints, obj, options); 
% fprintf('%s \n', diagnosis.info);
lp_obj = double(obj);

%{
* Round LP solution to retrieve outliers
%}
y = double(y);
[~, srt] = sort(y, 1, 'descend');
outliers = srt(1:n_outliers);

end
