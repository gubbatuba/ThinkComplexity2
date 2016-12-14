from statistics import mode

class Subhash():
    ''' Pick the most popular action, or the first
    '''
    def step(self, history, round):
            flatten = [item for sl in history for item in sl]
            action = mode(flatten)
        return action