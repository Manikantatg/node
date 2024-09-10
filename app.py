import os
import cv2
import numpy as np
import networkx as nx
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

def process_image(image_path):
    """Extract graph nodes and edges from an image using OpenCV."""
    # Load the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply edge detection (Canny Edge Detection)
    edges = cv2.Canny(img, 100, 200)

    # Use Hough Circles or similar method to detect circular nodes
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30, param1=50, param2=30, minRadius=10, maxRadius=30)

    nodes = []
    edges_detected = []

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        
        for (x, y, r) in circles:
            nodes.append((x, y))  # Treat the center of the circle as the node
        
        # Now you could use line detection (HoughLinesP) to detect edges
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=50, maxLineGap=10)
        if lines is not None:
            for line in lines:
                for x1, y1, x2, y2 in line:
                    edges_detected.append(((x1, y1), (x2, y2)))  # Store edges as tuples of coordinates

    return nodes, edges_detected

def build_graph(nodes, edges):
    """Build a graph from detected nodes and edges."""
    G = nx.Graph()

    # Add nodes
    for i, node in enumerate(nodes):
        G.add_node(i, pos=node)

    # Add edges
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]
        # Find the closest nodes based on positions
        n1 = min(G.nodes, key=lambda n: np.linalg.norm(np.array(G.nodes[n]['pos']) - np.array(node1)))
        n2 = min(G.nodes, key=lambda n: np.linalg.norm(np.array(G.nodes[n]['pos']) - np.array(node2)))
        G.add_edge(n1, n2)

    return G

def analyze_graph(image_path):
    nodes, edges = process_image(image_path)
    
    if not nodes or not edges:
        return {"error": "No graph detected"}

    G = build_graph(nodes, edges)

    # Example of path analysis:
    try:
        shortest_path = nx.shortest_path(G, source=0, target=len(nodes) - 1)
    except nx.NetworkXNoPath:
        shortest_path = []

    all_pairs_paths = dict(nx.all_pairs_dijkstra_path_length(G))
    max_len = 0
    longest_path = []
    for node, paths in all_pairs_paths.items():
        for target, length in paths.items():
            if length > max_len:
                max_len = length
                longest_path = nx.shortest_path(G, source=node, target=target)

    return {
        "shortPaths": shortest_path,
        "longPaths": longest_path,
        "numShortPaths": len(shortest_path) - 1,
        "numLongPaths": len(longest_path) - 1
    }

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'graphImage' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['graphImage']
    if file:
        # Save the uploaded image
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image_path)

        # Perform graph analysis
        result = analyze_graph(image_path)

        return jsonify(result)
    return jsonify({"error": "Error processing the file"}), 500

if __name__ == '__main__':
    app.run(debug=True)
