#
import argparse
import json
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, SetupOptions
from dataflow.common.masking_utils import mask_pii

class ParseMessage(beam.DoFn):
    def process(self, element):
        record = json.loads(element.decode('utf-8'))
        yield mask_pii(record)

def run(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_subscription', required=True)
    parser.add_argument('--output_table', required=True)
    known_args, pipeline_args = parser.parse_known_args(argv)

    pipeline_options = PipelineOptions(pipeline_args, streaming=True)
    pipeline_options.view_as(SetupOptions).save_main_session = True

    with beam.Pipeline(options=pipeline_options) as p:
        (p | 'ReadFromPubSub' >> beam.io.ReadFromPubSub(subscription=known_args.input_subscription)
           | 'ParseAndMask' >> beam.ParDo(ParseMessage())
           | 'WriteToBQ' >> beam.io.WriteToBigQuery(
                known_args.output_table,
                schema='EmployeeID:INTEGER,FirstName:STRING,LastName:STRING,Email:STRING',
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
            ))

if __name__ == '__main__':
    run()
