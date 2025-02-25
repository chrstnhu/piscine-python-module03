from Kmeans import KmeansClustering
import sys
import os

def error_exit():
    print("Usage: python main.py filepath='../ressources/solar_system_census.csv' ncentroid=4 max_iter=30")
    exit()

def check_path(argv):
    if 'filepath' in argv:
        filepath = argv.split('=')[1]
        if not filepath.endswith(".csv") and isinstance(filepath, str):
            return None
        if not os.path.exists(filepath):
            return None
        return filepath
    return None


def check_ncentroid(argv):
    if 'ncentroid' in argv:
        try :
            ncentroid = int(argv.split('=')[1])
            if ncentroid <= 0:
                return None
            return ncentroid
        except ValueError:
            return None
    return None

def check_max_iter(argv):
    if 'max_iter' in argv:
        try :
            max_iter = int(argv.split('=')[1])
            if max_iter <= 0:
                return None
            return max_iter
        except ValueError:
            return None
    return None


# Main
if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Here")
        error_exit()

    # Check if arguments are correct
    filepath = check_path(sys.argv[1])
    ncentroid = check_ncentroid(sys.argv[2])
    max_iter = check_max_iter(sys.argv[3])

    if filepath is None or ncentroid is None or max_iter is None:
        error_exit()
    else:
        print("Check ok")

    # Load the data
    kmeans = KmeansClustering(max_iter=max_iter, ncentroid=ncentroid)
    # kmeans.fit(filepath)
    # kmeans.predict(filepath)