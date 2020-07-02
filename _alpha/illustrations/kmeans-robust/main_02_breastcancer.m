clear; rng default; 

% read file
fid = fopen('breastcancer_dataset.txt');
data = textscan(fid, '%*s %s %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f', 'Delimiter', ',');
fclose(fid);

observations = [];
for i = 2:31
    observations = [observations, data{i}]; %#ok<AGROW>
end
observations = observations';

% normalize dataset if needed
observations = zscore(observations')';

N = length(data{1});
label = zeros(N,1);
for i = 1:N
    diagnosis = data{1}(i);
    if strcmp(diagnosis, 'M')        % malignant (bad)
        label(i) = 2;
    elseif strcmp(diagnosis, 'B')    % benign (good)
        label(i) = 1;
    end
end


sizes = [sum(label == 1), sum(label == 2)];
K = length(sizes);

%{
* Kmeans (LP) with cardinality constraints
%}
outliers_all = 0:4:sum(sizes);
cluster_all = zeros(N, length(outliers_all));
dist_ub_all = zeros(1, length(outliers_all));
dist_lb_all = zeros(1, length(outliers_all));

for i = 1:length(outliers_all)

outliers = outliers_all(i);    
    
[cluster, dist_ub, dist_lb] = kmean_lp_balanced(observations, 1, outliers);
cluster_all(:,i) = cluster; 
dist_ub_all(i) = dist_ub;
dist_lb_all(i) = dist_lb;

cluster_size = [sum(cluster == +1), ...
                sum(cluster == -1)];
fprintf(' > suboptimality = %4f\n', dist_ub/dist_lb);
fprintf(' > resulting cardinalities = %2d, %2d \n', cluster_size);
fprintf(' > sum-of-square distance = %4f \n', dist_ub);

end
