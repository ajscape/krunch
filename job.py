class Job:
    def __init__(self):
        self._input_file = None
        self._num_partitions = 3
        self._map_fn = None
        self._reduce_fn = None
        self._output_file = None

    def read_file(self, filepath):
        self._input_file = filepath
        return self

    def map(self, fn):
        self._map_fn = fn
        return self

    def reduce(self, fn):
        self._reduce_fn = fn
        return self

    def write_file(self, filepath):
        self._output_file = filepath
        return self

    def get_input_file(self):
        return self._input_file

    def get_output_file(self):
        return self._output_file

    def get_map_fn(self):
        return self._map_fn

    def get_reduce_fn(self):
        return self._reduce_fn

    def get_num_partitions(self):
        return self._num_partitions
