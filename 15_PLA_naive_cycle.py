import utilities as ut
DATA_PATH = 'hw1_15_train.dat'

def main():
    features, decisions = ut.load_file(DATA_PATH)
    loop_cycling_thru, last_training_index = ut.train(features, decisions)
    print ('loop thru {0}, last training data index {1}'.format(loop_cycling_thru, last_training_index))

if __name__ == '__main__':
    main()
