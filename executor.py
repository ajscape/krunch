from computeclient import ComputeClient
from job import Job
from storageclient import StorageClient


class Executor:
    def __init__(self):
        self._compute = ComputeClient()
        self._storage = StorageClient()

    def run(self, job: Job):
        n = job.get_num_partitions()

        infile_id = self.upload_file(job.get_input_file())
        mapfn_id = self.upload_fn(job.get_map_fn())
        reducefn_id = self.upload_fn(job.get_reduce_fn())

        split_out = self.run_split_fn(infile_id, n)

        # map
        map_outputs = {}
        for i, file_id in split_out:
            map_outputs[i] = self.run_map_fn(mapfn_id, file_id, n)

        # shuffle
        reduce_inputs = self.shuffle(map_outputs)

        # reduce
        reduce_file_ids = {}
        for i, file_ids in reduce_inputs:
            reduce_file_ids[i] = self.run_reduce_fn(reducefn_id, file_ids)

        outfile_id = self.run_combine_fn(reduce_file_ids)
        self.download_file(outfile_id, job.get_output_file())

    def run_split_fn(self, infile_id, n):
        return ['f1', 'f2', 'f3']

    def run_map_fn(self, mapfn_id, infile_id, n):
        return ['f1-p1', 'f2-p1', 'f3-p1']

    def shuffle(self, map_inputs):
        #todo
        return 0

    def run_reduce_fn(self, reducefn_id, infile_ids):
        return ['f1-p1', 'f2-p1', 'f3-p1']

    def run_combine_fn(self, infile_ids):
        return 0

    def upload_file(self, filepath):
        text = self.read_text_file(filepath)
        return self._storage.write(self, text)

    def download_file(self, file_id, out_filepath):
        text = self._storage.read(file_id)
        self.write_text_file(text, out_filepath)

    def upload_fn(self, fn):
        # todo: pickle
        return self._storage.write(fn)

    def read_text_file(self, filepath):
        # todo
        return filepath

    def write_text_file(self, text, filepath):
        # todo
        return
