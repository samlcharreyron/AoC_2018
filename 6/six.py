import sys
import numpy as np

def generate_single_map(p_a, cols=10, rows=10):
    m = np.zeros((cols, rows), np.int)
    yg, xg = np.meshgrid(np.arange(0, rows), np.arange(0, cols))
    return np.abs(p_a[0] - xg).astype(np.int) + np.abs(p_a[1] - yg).astype(np.int)

def isin(element, test_elements, assume_unique=False, invert=False):
    "..."
    element = np.asarray(element)
    return np.in1d(element, test_elements, assume_unique=assume_unique,
                invert=invert).reshape(element.shape)

def p1(P, cols=10, rows=10):
    N = P.shape[0]

    m = sys.maxint * np.ones((cols, rows, N), np.int)
    for i in xrange(N):
        m[:,:,i] = generate_single_map(P[i,:], cols, rows)
    m_ = np.argmin(m, axis=2) 

    # remove duplicate points
    mask = np.zeros(m_.shape, np.bool)
    for j in xrange(m_.shape[1]):
	for i in xrange(m_.shape[0]):
	    if len(np.where(m[i,j, :] == np.min(m[i, j, :]))[0]) > 1:
		mask[i,j] = True
    m_[mask] = -1

    # find edge points
    ymin, xmin = np.min(P, axis=0).astype(np.int)
    ymax, xmax = np.max(P, axis=0).astype(np.int)

    x = np.arange(xmin, xmax)
    y = np.arange(ymin, ymax)

    edges = np.concatenate((np.unique(m_[y,xmin]),
        np.unique(m_[y, xmax]),
        np.unique(m_[ymin, x]),
        np.unique(m_[ymax, x])))
    
    mask = np.logical_not(isin(m_, edges))
    
    _, counts = np.unique(m_[mask], return_counts=True)
    return np.max(counts)

def p2(P, thresh=10000, cols=500, rows=500):
    N = P.shape[0]

    m = sys.maxint * np.ones((cols, rows, N), np.int)
    for i in xrange(N):
        m[:,:,i] = generate_single_map(P[i,:], cols, rows)
    return np.sum(np.sum(m, axis=2) < thresh)


if __name__ == '__main__':
    points = np.loadtxt(sys.argv[1], delimiter=',')
    print p1(points, cols=500, rows=500)
    print p2(points, thresh=10000, cols=500, rows=500)

