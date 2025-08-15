from ultralytics import YOLO
import cv2
import numpy as np

def run_yolo_inference(model_path, image_path, conf_threshold=0.25, iou_threshold=0.45):
    # Load the YOLO model using the ultralytics package
    model = YOLO(model_path)
    
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image at {image_path}")
        return
    
    # Run inference with specified parameters
    results = model(img, conf=conf_threshold, iou=iou_threshold)[0]
    
    # Create a copy of the image for visualization
    img_vis = img.copy()
    
    print("Detection results:")
    print("Class\tConfidence\tCenter X\tCenter Y\tBottom X\tBottom Y")
    
    # Process each detection
    for box in results.boxes:
        # Get box coordinates
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        
        # Calculate center point
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        
        # Calculate bottom-most point on the center line
        bottom_x = center_x
        bottom_y = y2
        
        # Get confidence and class
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        
        # Get class name
        class_name = results.names[cls]
        
        # Draw bounding box
        cv2.rectangle(img_vis, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Draw center point
        cv2.circle(img_vis, (int(center_x), int(center_y)), 5, (0, 0, 255), -1)
        
        # Draw bottom-most point
        cv2.circle(img_vis, (int(bottom_x), int(bottom_y)), 5, (255, 0, 0), -1)
        
        # Add label
        label = f"{class_name} {conf:.2f}"
        t_size = cv2.getTextSize(label, 0, fontScale=0.6, thickness=1)[0]
        c2 = x1 + t_size[0], y1 - t_size[1] - 3
        cv2.rectangle(img_vis, (x1, y1), c2, (0, 255, 0), -1, cv2.LINE_AA)  # filled
        cv2.putText(img_vis, label, (x1, y1 - 2), 0, 0.6, (0, 0, 0), thickness=1, lineType=cv2.LINE_AA)
        
        # Print information
        print(f"{class_name}\t{conf:.2f}\t{center_x:.1f}\t{center_y:.1f}\t{bottom_x:.1f}\t{bottom_y:.1f}")
    
    # Save the visualization
    output_path = 'detection_result.jpg'
    cv2.imwrite(output_path, img_vis)
    print(f"Visualization saved as '{output_path}'")
    
    # Display the image with detections
    cv2.imshow("YOLO Detection", img_vis)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return results, img_vis

if __name__ == "__main__":
    # Replace these with your actual paths
    MODEL_PATH = "best_fire2.pt"
    IMAGE_PATH = "fire_img.jpg"
    
    # Run inference
    results, _ = run_yolo_inference(MODEL_PATH, IMAGE_PATH)