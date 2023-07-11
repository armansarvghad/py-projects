import cv2
import torch
import torchvision.transforms as T
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import Visualizer

# Load the pre-trained instance segmentation model
model_path = 'path_to_model_weights'
cfg = get_cfg()
cfg.merge_from_file('path_to_config_file')
cfg.MODEL.WEIGHTS = model_path
predictor = DefaultPredictor(cfg)

# Load and preprocess the image
image = cv2.imread('path_to_image')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
transform = T.Compose([T.ToTensor()])
image_tensor = transform(image_rgb)

# Make predictions
outputs = predictor(image_tensor.unsqueeze(0))
instances = outputs["instances"].to(torch.device("cpu"))

# Visualize the predictions
v = Visualizer(image_rgb, metadata=cfg.DATASETS.TEST[0])
v = v.draw_instance_predictions(instances)
result_image = v.get_image()

# Display the result
cv2.imshow("Instance Segmentation", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
