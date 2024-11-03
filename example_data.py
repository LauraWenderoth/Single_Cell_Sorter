import kagglehub

# Download latest version
path = kagglehub.dataset_download("andrewmvd/bone-marrow-cell-classification")

print("Path to dataset files:", path)
