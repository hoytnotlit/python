import numpy as np


def masked_mean(matrix, mask):
    """
    given a 4D matrix A and a 3D mask B return a 3D matrix C where the third and last dimension
    is the average over the third dimension in 4D.

    lets say we have a matrix where with the dims are (NR DOCUMENTS, NR SENTENCE, NR WORDS, WORD FEATURE DIM),
    (WORD FEATURE DIM is the length of the feature vectors we use to represent words)

    example:
    M = [
        [[w1,w2,pad,pad],[w1,w2,w3,pad]],
        [[w1,pad,pad,pad],[w1,w2,pad,pad]],
        ...
        [[w1,w2,pad,pad],[w1,w2,w3,pad]],
        ]
    NOTE! wn here is a vector.

    we would then have a mask where mask[0] == [[1,1,0,0],[1,1,1,0]]. So, our mask signifies which words in each
    document that are pads or actual words.

    What we want to do is average M and create M2. M2 should contained vectors of sentences representations
    instead of a 2D matrix of word features e.g:

    M2 = [
        [sent1,sent2],
        [sent1,sent2],
        ...
        [sent1,sent2],
        ]
    where sentn is a vector

    when we are averaging we dont want to include the padding tokens hence we can use the mask to make
    sure we are averaging correctly.

    restrictions
    1) you are not allowed to use any loops instead you are suppose to use matrix operations

    """

    # STEP 1: do the masking
    # convert 'pad' values to nan
    masked = np.where(mask[..., None], matrix, np.nan)

    # STEP 2: do the mean
    # take mean along axis 2, ignoring nan
    meaned_arr = np.nanmean(masked, axis=2)

    return meaned_arr


def make_sample_matrices(nr_documents=2, nr_sentences=2, nr_words=4, nr_features=6):
    """
    Returns sample 4D matrix and 3D mask -> (matrix, mask)
    """
    # create sample matrix
    matrix = np.array(
        [
            [
                [np.random.randint(0, 10, size=nr_features) for _ in range(nr_words)]
                for _ in range(nr_sentences)
            ]
            for _ in range(nr_documents)
        ]
    )

    # create sample mask
    def add_pad(row):
        idx = np.random.randint(0, len(row)) + 1
        row[idx:] = 0
        return row

    mask = np.ones((nr_documents, nr_sentences, nr_words))
    np.apply_along_axis(add_pad, 2, mask)

    return matrix, mask


def test():
    """
    Create example M and mask matrices and pass into masked_mean
    """
    matrix, mask = make_sample_matrices()
    meaned_matrix = masked_mean(matrix, mask)

    # Print out all matrices
    print("\n" + "-" * 20)
    print(f"matrix {matrix.shape}:")
    print("-" * 20)
    print(matrix)

    print("\n" + "-" * 20)
    print(f"mask {mask.shape}:")
    print("-" * 20)
    print(mask)

    print("\n" + "-" * 20)
    print(f"result {meaned_matrix.shape}:")
    print("-" * 20)
    print(meaned_matrix)
    print()


if __name__ == "__main__":
    test()
