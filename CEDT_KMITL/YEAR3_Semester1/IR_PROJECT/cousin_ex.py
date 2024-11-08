import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import svd
np.set_printoptions(precision=3, suppress=True)

class CosineSimilarityExplanation:
    def __init__(self):
        self.fig_size = (10, 6)
    
    def plot_vectors(self, v1, v2, title="Vector Representation"):
        """Plot two 2D vectors to visualize angle between them"""
        plt.figure(figsize=self.fig_size)
        plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector 1')
        plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector 2')
        
        # Draw angle arc
        angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
        radius = 0.5
        angle_range = np.linspace(0, angle, 100)
        plt.plot(radius * np.cos(angle_range), radius * np.sin(angle_range), 'g--', label='θ')
        
        plt.axis('equal')
        plt.grid(True)
        plt.title(title)
        plt.legend()
        plt.show()
    
    def demonstrate_cosine_similarity(self):
        """Demonstrate cosine similarity calculation with steps"""
        # Example vectors
        v1 = np.array([3, 4])  # Vector 1
        v2 = np.array([4, 3])  # Vector 2
        
        # Step 1: Plot vectors
        self.plot_vectors(v1, v2, "Step 1: Vector Representation")
        
        # Step 2: Calculate dot product
        dot_product = np.dot(v1, v2)
        print("\nStep 2: Dot Product Calculation")
        print(f"dot_product = ({v1[0]} × {v2[0]}) + ({v1[1]} × {v2[1]})")
        print(f"            = {v1[0]*v2[0]} + {v1[1]*v2[1]}")
        print(f"            = {dot_product}")
        
        # Step 3: Calculate magnitudes
        magnitude_v1 = np.linalg.norm(v1)
        magnitude_v2 = np.linalg.norm(v2)
        print("\nStep 3: Calculate Vector Magnitudes")
        print(f"||v1|| = √({v1[0]}² + {v1[1]}²)")
        print(f"      = √{v1[0]**2 + v1[1]**2}")
        print(f"      = {magnitude_v1}")
        print(f"\n||v2|| = √({v2[0]}² + {v2[1]}²)")
        print(f"      = √{v2[0]**2 + v2[1]**2}")
        print(f"      = {magnitude_v2}")
        
        # Step 4: Calculate cosine similarity
        cosine_similarity = dot_product / (magnitude_v1 * magnitude_v2)
        print("\nStep 4: Calculate Cosine Similarity")
        print("cos(θ) = dot_product / (||v1|| × ||v2||)")
        print(f"      = {dot_product} / ({magnitude_v1} × {magnitude_v2})")
        print(f"      = {cosine_similarity}")
        
        # Step 5: Calculate angle
        angle = np.arccos(cosine_similarity)
        print(f"\nStep 5: Calculate Angle")
        print(f"θ = arccos({cosine_similarity})")
        print(f"  = {angle} radians")
        print(f"  = {np.degrees(angle)} degrees")
        
        return cosine_similarity, angle

# Example with text documents
def text_cosine_similarity_example():
    print("\nExample with Text Documents:")
    print("="*80)
    
    # Simple document vectors (TF-IDF representations)
    doc1 = np.array([0.5, 0.8, 0.3])  # Example document 1
    doc2 = np.array([0.2, 0.7, 0.5])  # Example document 2
    
    print("Document Vector 1:", doc1)
    print("Document Vector 2:", doc2)
    
    # Step 1: Dot product
    dot_product = np.dot(doc1, doc2)
    print("\nStep 1: Dot Product")
    print(f"dot_product = ({doc1[0]}×{doc2[0]}) + ({doc1[1]}×{doc2[1]}) + ({doc1[2]}×{doc2[2]})")
    print(f"           = {doc1[0]*doc2[0]:.3f} + {doc1[1]*doc2[1]:.3f} + {doc1[2]*doc2[2]:.3f}")
    print(f"           = {dot_product:.3f}")
    
    # Step 2: Calculate magnitudes
    magnitude_doc1 = np.linalg.norm(doc1)
    magnitude_doc2 = np.linalg.norm(doc2)
    
    print("\nStep 2: Vector Magnitudes")
    print(f"||doc1|| = √({doc1[0]}² + {doc1[1]}² + {doc1[2]}²)")
    print(f"        = √{sum(doc1**2):.3f}")
    print(f"        = {magnitude_doc1:.3f}")
    
    print(f"\n||doc2|| = √({doc2[0]}² + {doc2[1]}² + {doc2[2]}²)")
    print(f"        = √{sum(doc2**2):.3f}")
    print(f"        = {magnitude_doc2:.3f}")
    
    # Step 3: Cosine similarity
    cosine_sim = dot_product / (magnitude_doc1 * magnitude_doc2)
    print("\nStep 3: Cosine Similarity")
    print(f"cos(θ) = {dot_product:.3f} / ({magnitude_doc1:.3f} × {magnitude_doc2:.3f})")
    print(f"       = {dot_product:.3f} / {(magnitude_doc1 * magnitude_doc2):.3f}")
    print(f"       = {cosine_sim:.3f}")
    
    return cosine_sim

# Run demonstrations
demo = CosineSimilarityExplanation()
print("Geometric Derivation of Cosine Similarity")
print("="*80)
cosine_sim, angle = demo.demonstrate_cosine_similarity()

# Text document example
text_sim = text_cosine_similarity_example()