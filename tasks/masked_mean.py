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

    # maybe there is something to work on here? values get masked but the matrix is 
    # flattened to two dimensions
    mask_bool = np.array(mask, dtype=bool)
    masked = matrix[mask_bool]

    # STEP 2: do the mean
    meaned_arr = np.mean(matrix, axis=2)

    return meaned_arr


def test():
    """
    Create example M and mask matrices and pass into masked_mean
    """

    # set parameters
    nr_documents = 2
    nr_sentences = 2
    nr_words = 4
    nr_features = 2

    # create sample M
    matrix = np.array(
        [
            [
                [np.random.rand(nr_features) for _ in range(nr_words)]
                for _ in range(nr_sentences)
            ]
            for _ in range(nr_documents)
        ]
    )

    # create sample mask
    mask = np.array(
        [
            [np.random.randint(0, 2, nr_words) for _ in range(nr_sentences)]
            for _ in range(nr_documents)
        ]
    )

    masked_mean(matrix, mask)


if __name__ == "__main__":
    test()