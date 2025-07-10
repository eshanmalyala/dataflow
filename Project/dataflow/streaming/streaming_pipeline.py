import json
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam.io.gcp.pubsub import ReadFromPubSub

from common.masking_utils import mask_email, mask_phone

class ParseAndMaskDoFn(beam.DoFn):
    def process(self, message):
        row = json.loads(message.decode("utf-8"))
        row['email'] = mask_email(row.get('email', ''))
        row['phone'] = mask_phone(row.get('phone', ''))
        yield row

def run():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_subscription', required=True)
    parser.add_argument('--output_table', required=True)
    args, beam_args = parser.parse_known_args()

    pipeline_options = PipelineOptions(beam_args, streaming=True, save_main_session=True)

    with beam.Pipeline(options=pipeline_options) as p:
        (
            p
            | 'ReadFromPubSub' >> ReadFromPubSub(subscription=args.input_subscription)
            | 'ParseAndMask' >> beam.ParDo(ParseAndMaskDoFn())
            | 'WriteToBigQuery' >> WriteToBigQuery(
                args.output_table,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
            )
        )

if __name__ == '__main__':
    run()


# #
# import argparse
# import json
# import apache_beam as beam
# from apache_beam.options.pipeline_options import PipelineOptions, SetupOptions
# from dataflow.common.masking_utils import mask_pii

# class ParseMessage(beam.DoFn):
#     def process(self, element):
#         record = json.loads(element.decode('utf-8'))
#         yield mask_pii(record)

# def run(argv=None):
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--input_subscription', required=True)
#     parser.add_argument('--output_table', required=True)
#     known_args, pipeline_args = parser.parse_known_args(argv)

#     pipeline_options = PipelineOptions(pipeline_args, streaming=True)
#     pipeline_options.view_as(SetupOptions).save_main_session = True

#     with beam.Pipeline(options=pipeline_options) as p:
#         (p | 'ReadFromPubSub' >> beam.io.ReadFromPubSub(subscription=known_args.input_subscription)
#            | 'ParseAndMask' >> beam.ParDo(ParseMessage())
#            | 'WriteToBQ' >> beam.io.WriteToBigQuery(
#                 known_args.output_table,
#                 schema='EmployeeID:INTEGER,FirstName:STRING,LastName:STRING,Email:STRING',
#                 write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
#             ))

# if __name__ == '__main__':
#     run()
