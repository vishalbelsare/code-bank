#!/bin/sh


for review in ../data/pdf_reviews/*.md; do
    review_pdf="${review/.md/.pdf}" # replace .md with .pdf
    pandoc $review -o $review_pdf
done
