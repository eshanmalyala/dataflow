import argparse
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from common import masking_utils

class MaskSensitiveData(beam.DoFn):
    def process(self, element):
        import json
        record = json.loads(element)
        record['email'] = masking_utils.mask_email(record.get('email', ''))
        record['phone'] = masking_utils.mask_phone(record.get('phone', ''))
        yield record

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', required=True)
    parser.add_argument('--output_table', required=True)
    args, pipeline_args = parser.parse_known_args()

    options = PipelineOptions(pipeline_args, save_main_session=True, streaming=False)

    with beam.Pipeline(options=options) as p:
        (
            p
            | 'Read from GCS' >> beam.io.ReadFromText(args.input_path)
            | 'Mask PII' >> beam.ParDo(MaskSensitiveData())
            | 'Write to BQ' >> beam.io.WriteToBigQuery(
                args.output_table,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
            )
        )

if __name__ == '__main__':
    run()
