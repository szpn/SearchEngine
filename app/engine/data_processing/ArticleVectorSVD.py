import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import normalize
import scipy as sp

class ArticleVectorSVD:
    def __init__(self, input_vector_path, output_vector_path, k):
        self.input_vector_path = input_vector_path
        self.output_vector_path = output_vector_path
        self.k = k

    def run(self):
        self.compute_truncated_svd()

    def compute_truncated_svd(self):
        print("Loading TBD matrix...")
        TBD_matrix = sp.sparse.load_npz(self.input_vector_path)

        print("Computing Truncated SVD...")
        svd = TruncatedSVD(n_components=self.k)
        US = svd.fit_transform(TBD_matrix)
        Vh = svd.components_

        US = normalize(US, axis=1, norm='l2')
        Vh = normalize(Vh, axis=0, norm='l2')


        print("Saving Truncated SVD matrix...")
        np.savez(self.output_vector_path, US=US, Vh=Vh)


if __name__ == "__main__":
    TBD_path = "../data/term_by_document.npz"
    output_file = "../data/US_Vh_matrices_2500.npz"
    k = 2500

    svd_processor = ArticleVectorSVD(TBD_path, output_file, k)
    svd_processor.run()
