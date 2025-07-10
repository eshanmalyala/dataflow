### issue 1: 
rajasekhar_malyala@cloudshell:~/dataflow/Project (gcp-agent-garden)$ gcloud builds submit --config=cicd/cloudbuild.yaml
Creating temporary archive of 19 file(s) totalling 9.3 KiB before compression.
Uploading tarball of [.] to [gs://gcp-agent-garden_cloudbuild/source/1752132021.876196-0ce2f86916ef4339a08aba366c58b177.tgz]
ERROR: (gcloud.builds.submit) INVALID_ARGUMENT: generic::invalid_argument: invalid value for 'build.substitutions': key in the template "BUCKET" is not a valid built-in substitution

 ### fix  the issue:  
  "$$"  In cloud build args , variables like $BUCKET are missinterprted unless escaped 
   $$BUCKET tells cloud build this is a bash variable , don't try to substitute it

### issue 2


default-hostname
*** Reading remote logs from Cloud Logging.
[2025-07-10, 08:46:52 UTC] {local_task_job_runner.py:123} ▼ Pre task execution logs
[2025-07-10, 08:46:52 UTC] {taskinstance.py:2616} INFO - Dependencies all met for dep_context=non-requeueable deps ti=<TaskInstance: trigger_streaming_dataflow_job.start_streaming_flex_job manual__2025-07-10T08:46:49.428570+00:00 [queued]>
[2025-07-10, 08:46:52 UTC] {taskinstance.py:2616} INFO - Dependencies all met for dep_context=requeueable deps ti=<TaskInstance: trigger_streaming_dataflow_job.start_streaming_flex_job manual__2025-07-10T08:46:49.428570+00:00 [queued]>
[2025-07-10, 08:46:52 UTC] {taskinstance.py:2869} INFO - Starting attempt 1 of 3
[2025-07-10, 08:46:52 UTC] {taskinstance.py:2892} INFO - Executing <Task(DataflowStartFlexTemplateOperator): start_streaming_flex_job> on 2025-07-10 08:46:49.428570+00:00
[2025-07-10, 08:46:52 UTC] {standard_task_runner.py:72} INFO - Started process 85105 to run task
[2025-07-10, 08:46:52 UTC] {standard_task_runner.py:104} INFO - Running: ['airflow', 'tasks', 'run', 'trigger_streaming_dataflow_job', 'start_streaming_flex_job', 'manual__2025-07-10T08:46:49.428570+00:00', '--job-id', '486', '--raw', '--subdir', 'DAGS_FOLDER/streaming_dataflow_trigger_dag.py', '--cfg-path', '/tmp/tmpvyh1nxmc']
[2025-07-10, 08:46:52 UTC] {standard_task_runner.py:105} INFO - Job 486: Subtask start_streaming_flex_job
[2025-07-10, 08:46:52 UTC] {task_command.py:473} INFO - Running <TaskInstance: trigger_streaming_dataflow_job.start_streaming_flex_job manual__2025-07-10T08:46:49.428570+00:00 [running]> on host airflow-worker-m8678
[2025-07-10, 08:46:53 UTC] {taskinstance.py:3136} INFO - Exporting env vars: AIRFLOW_CTX_DAG_OWNER='airflow' AIRFLOW_CTX_DAG_ID='trigger_streaming_dataflow_job' AIRFLOW_CTX_TASK_ID='start_streaming_flex_job' AIRFLOW_CTX_EXECUTION_DATE='2025-07-10T08:46:49.428570+00:00' AIRFLOW_CTX_TRY_NUMBER='1' AIRFLOW_CTX_DAG_RUN_ID='manual__2025-07-10T08:46:49.428570+00:00'
[2025-07-10, 08:46:53 UTC] {taskinstance.py:733} ▲▲▲ Log group end
[2025-07-10, 08:46:53 UTC] {dataflow.py:632} INFO - Job name was changed to streaming-pii-job-20250710-14c76bd5
[2025-07-10, 08:46:54 UTC] {base.py:84} INFO - Retrieving connection 'google_cloud_default'
[2025-07-10, 08:46:54 UTC] {credentials_provider.py:410} INFO - Getting connection using `google.auth.default()` since no explicit credentials are provided.
[2025-07-10, 08:46:54 UTC] {google_auth_httplib2.py:112} WARNING - httplib2 transport does not support per-request timeout. Set the timeout when constructing the httplib2.Http instance.
[2025-07-10, 08:46:54 UTC] {google_auth_httplib2.py:112} WARNING - httplib2 transport does not support per-request timeout. Set the timeout when constructing the httplib2.Http instance.
[2025-07-10, 08:46:54 UTC] {taskinstance.py:3315} ERROR - Task failed with exception
Traceback (most recent call last):
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 769, in _execute_task
    result = _execute_callable(context=context, **execute_callable_kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 735, in _execute_callable
    return ExecutionCallableRunner(
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/utils/operator_helpers.py", line 252, in run
    return self.func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/baseoperator.py", line 424, in wrapper
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/providers/google/cloud/operators/dataflow.py", line 596, in execute
    self.job = self.hook.start_flex_template(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/providers/google/common/hooks/base_google.py", line 532, in inner_wrapper
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/providers/google/cloud/hooks/dataflow.py", line 820, in start_flex_template
    response: dict = request.execute(num_retries=self.num_retries)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/googleapiclient/_helpers.py", line 130, in positional_wrapper
    return wrapped(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/googleapiclient/http.py", line 938, in execute
    raise HttpError(resp, content, uri=self.uri)
googleapiclient.errors.HttpError: <HttpError 404 when requesting https://dataflow.googleapis.com/v1b3/projects/gcp-agent-garden/locations/europe-west1/flexTemplates:launch?alt=json returned "(710ce26244e56f58): Unable to open template file: gs://getwellsoon-bucket/templates/streaming_template.json.". Details: "(710ce26244e56f58): Unable to open template file: gs://getwellsoon-bucket/templates/streaming_template.json.">
[2025-07-10, 08:46:54 UTC] {taskinstance.py:1227} INFO - Marking task as UP_FOR_RETRY. dag_id=trigger_streaming_dataflow_job, task_id=start_streaming_flex_job, run_id=manual__2025-07-10T08:46:49.428570+00:00, execution_date=20250710T084649, start_date=20250710T084652, end_date=20250710T084654
[2025-07-10, 08:46:55 UTC] {taskinstance.py:341} ▼ Post task execution logs
[2025-07-10, 08:46:55 UTC] {standard_task_runner.py:124} ERROR - Failed to execute job 486 for task start_streaming_flex_job (<HttpError 404 when requesting https://dataflow.googleapis.com/v1b3/projects/gcp-agent-garden/locations/europe-west1/flexTemplates:launch?alt=json returned "(710ce26244e56f58): Unable to open template file: gs://getwellsoon-bucket/templates/streaming_template.json.". Details: "(710ce26244e56f58): Unable to open template file: gs://getwellsoon-bucket/templates/streaming_template.json.">; 85105)
Traceback (most recent call last):
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/task/task_runner/standard_task_runner.py", line 117, in _start_by_fork
    ret = args.func(args, dag=self.dag)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/cli/cli_config.py", line 49, in command
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/utils/cli.py", line 116, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/cli/commands/task_command.py", line 489, in task_run
    task_return_code = _run_task_by_selected_method(args, _dag, ti)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/cli/commands/task_command.py", line 256, in _run_task_by_selected_method
    return _run_raw_task(args, ti)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/cli/commands/task_command.py", line 341, in _run_raw_task
    return ti._run_raw_task(
           ^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/utils/session.py", line 97, in wrapper
    return func(*args, session=session, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 3008, in _run_raw_task
    return _run_raw_task(
           ^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 274, in _run_raw_task
    TaskInstance._execute_task_with_callbacks(
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 3163, in _execute_task_with_callbacks
    result = self._execute_task(context, task_orig)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 3187, in _execute_task
    return _execute_task(self, context, task_orig)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 769, in _execute_task
    result = _execute_callable(context=context, **execute_callable_kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 735, in _execute_callable
    return ExecutionCallableRunner(
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/utils/operator_helpers.py", line 252, in run
    return self.func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/baseoperator.py", line 424, in wrapper
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/providers/google/cloud/operators/dataflow.py", line 596, in execute
    self.job = self.hook.start_flex_template(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/providers/google/common/hooks/base_google.py", line 532, in inner_wrapper
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/providers/google/cloud/hooks/dataflow.py", line 820, in start_flex_template
    response: dict = request.execute(num_retries=self.num_retries)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/googleapiclient/_helpers.py", line 130, in positional_wrapper
    return wrapped(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/googleapiclient/http.py", line 938, in execute
    raise HttpError(resp, content, uri=self.uri)
googleapiclient.errors.HttpError: <HttpError 404 when requesting https://dataflow.googleapis.com/v1b3/projects/gcp-agent-garden/locations/europe-west1/flexTemplates:launch?alt=json returned "(710ce26244e56f58): Unable to open template file: gs://getwellsoon-bucket/templates/streaming_template.json.". Details: "(710ce26244e56f58): Unable to open template file: gs://getwellsoon-bucket/templates/streaming_template.json.">
[2025-07-10, 08:46:55 UTC] {local_task_job_runner.py:266} INFO - Task exited with return code 1
[2025-07-10, 08:46:55 UTC] {taskinstance.py:3904} INFO - 0 downstream tasks scheduled from follow-on schedule check
[2025-07-10, 08:46:55 UTC] {local_task_job_runner.py:245} ▲▲▲ Log group end


# #issue  3


default-hostname
*** Reading remote logs from Cloud Logging.
[2025-07-10, 09:02:01 UTC] {local_task_job_runner.py:123} ▶ Pre task execution logs
[2025-07-10, 09:02:03 UTC] {dataflow.py:632} INFO - Job name was changed to streaming-pii-job-20250710-e310b654
[2025-07-10, 09:02:03 UTC] {base.py:84} INFO - Retrieving connection 'google_cloud_default'
[2025-07-10, 09:02:03 UTC] {credentials_provider.py:410} INFO - Getting connection using `google.auth.default()` since no explicit credentials are provided.
[2025-07-10, 09:02:03 UTC] {google_auth_httplib2.py:112} WARNING - httplib2 transport does not support per-request timeout. Set the timeout when constructing the httplib2.Http instance.
[2025-07-10, 09:02:03 UTC] {google_auth_httplib2.py:112} WARNING - httplib2 transport does not support per-request timeout. Set the timeout when constructing the httplib2.Http instance.
[2025-07-10, 09:02:05 UTC] {http.py:140} WARNING - Encountered 403 Forbidden with reason "PERMISSION_DENIED"
[2025-07-10, 09:02:05 UTC] {taskinstance.py:3315} ERROR - Task failed with exception
Traceback (most recent call last):
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 769, in _execute_task
    result = _execute_callable(context=context, **execute_callable_kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 735, in _execute_callable
    return ExecutionCallableRunner(
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/utils/operator_helpers.py", line 252, in run
    return self.func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/baseoperator.py", line 424, in wrapper
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/providers/google/cloud/operators/dataflow.py", line 596, in execute
    self.job = self.hook.start_flex_template(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/providers/google/common/hooks/base_google.py", line 532, in inner_wrapper
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/providers/google/cloud/hooks/dataflow.py", line 820, in start_flex_template
    response: dict = request.execute(num_retries=self.num_retries)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/googleapiclient/_helpers.py", line 130, in positional_wrapper
    return wrapped(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/googleapiclient/http.py", line 938, in execute
    raise HttpError(resp, content, uri=self.uri)
googleapiclient.errors.HttpError: <HttpError 403 when requesting https://dataflow.googleapis.com/v1b3/projects/gcp-agent-garden/locations/europe-west1/flexTemplates:launch?alt=json returned "(ba5f06a874b0caf6): Current user cannot act as service account 1051082499499-compute@developer.gserviceaccount.com. Enforced by Org Policy constraint constraints/dataflow.enforceComputeDefaultServiceAccountCheck. https://cloud.google.com/iam/docs/service-accounts-actas Causes: (ba5f06a874b0c79e): Current user  cannot act as service account 1051082499499-compute@developer.gserviceaccount.com. If the service account belongs to the current project, please grant your user account one of [Owner, Editor, Service Account User] roles, or any other role that includes the iam.serviceAccounts.actAs permission. See https://cloud.google.com/iam/docs/service-accounts-actas for additional details. If the service account belongs to another project, please disable the iam.disableCrossProjectServiceAccountUsage org-policy constraint on the project the service account belongs to. See https://cloud.google.com/iam/docs/attach-service-accounts#attaching-different-project for additional details.". Details: "(ba5f06a874b0caf6): Current user cannot act as service account 1051082499499-compute@developer.gserviceaccount.com. Enforced by Org Policy constraint constraints/dataflow.enforceComputeDefaultServiceAccountCheck. https://cloud.google.com/iam/docs/service-accounts-actas Causes: (ba5f06a874b0c79e): Current user  cannot act as service account 1051082499499-compute@developer.gserviceaccount.com. If the service account belongs to the current project, please grant your user account one of [Owner, Editor, Service Account User] roles, or any other role that includes the iam.serviceAccounts.actAs permission. See https://cloud.google.com/iam/docs/service-accounts-actas for additional details. If the service account belongs to another project, please disable the iam.disableCrossProjectServiceAccountUsage org-policy constraint on the project the service account belongs to. See https://cloud.google.com/iam/docs/attach-service-accounts#attaching-different-project for additional details.">
[2025-07-10, 09:02:05 UTC] {taskinstance.py:1227} INFO - Marking task as UP_FOR_RETRY. dag_id=trigger_streaming_dataflow_job, task_id=start_streaming_flex_job, run_id=manual__2025-07-10T09:01:57.702078+00:00, execution_date=20250710T090157, start_date=20250710T090201, end_date=20250710T090205
[2025-07-10, 09:02:05 UTC] {taskinstance.py:341} ▼ Post task execution logs
[2025-07-10, 09:02:05 UTC] {standard_task_runner.py:124} ERROR - Failed to execute job 491 for task start_streaming_flex_job (<HttpError 403 when requesting https://dataflow.googleapis.com/v1b3/projects/gcp-agent-garden/locations/europe-west1/flexTemplates:launch?alt=json returned "(ba5f06a874b0caf6): Current user cannot act as service account 1051082499499-compute@developer.gserviceaccount.com. Enforced by Org Policy constraint constraints/dataflow.enforceComputeDefaultServiceAccountCheck. https://cloud.google.com/iam/docs/service-accounts-actas Causes: (ba5f06a874b0c79e): Current user  cannot act as service account 1051082499499-compute@developer.gserviceaccount.com. If the service account belongs to the current project, please grant your user account one of [Owner, Editor, Service Account User] roles, or any other role that includes the iam.serviceAccounts.actAs permission. See https://cloud.google.com/iam/docs/service-accounts-actas for additional details. If the service account belongs to another project, please disable the iam.disableCrossProjectServiceAccountUsage org-policy constraint on the project the service account belongs to. See https://cloud.google.com/iam/docs/attach-service-accounts#attaching-different-project for additional details.". Details: "(ba5f06a874b0caf6): Current user cannot act as service account 1051082499499-compute@developer.gserviceaccount.com. Enforced by Org Policy constraint constraints/dataflow.enforceComputeDefaultServiceAccountCheck. https://cloud.google.com/iam/docs/service-accounts-actas Causes: (ba5f06a874b0c79e): Current user  cannot act as service account 1051082499499-compute@developer.gserviceaccount.com. If the service account belongs to the current project, please grant your user account one of [Owner, Editor, Service Account User] roles, or any other role that includes the iam.serviceAccounts.actAs permission. See https://cloud.google.com/iam/docs/service-accounts-actas for additional details. If the service account belongs to another project, please disable the iam.disableCrossProjectServiceAccountUsage org-policy constraint on the project the service account belongs to. See https://cloud.google.com/iam/docs/attach-service-accounts#attaching-different-project for additional details.">; 85415)
Traceback (most recent call last):
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/task/task_runner/standard_task_runner.py", line 117, in _start_by_fork
    ret = args.func(args, dag=self.dag)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/cli/cli_config.py", line 49, in command
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/utils/cli.py", line 116, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/cli/commands/task_command.py", line 489, in task_run
    task_return_code = _run_task_by_selected_method(args, _dag, ti)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/cli/commands/task_command.py", line 256, in _run_task_by_selected_method
    return _run_raw_task(args, ti)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/cli/commands/task_command.py", line 341, in _run_raw_task
    return ti._run_raw_task(
           ^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/utils/session.py", line 97, in wrapper
    return func(*args, session=session, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 3008, in _run_raw_task
    return _run_raw_task(
           ^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 274, in _run_raw_task
    TaskInstance._execute_task_with_callbacks(
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 3163, in _execute_task_with_callbacks
    result = self._execute_task(context, task_orig)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 3187, in _execute_task
    return _execute_task(self, context, task_orig)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 769, in _execute_task
    result = _execute_callable(context=context, **execute_callable_kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/taskinstance.py", line 735, in _execute_callable
    return ExecutionCallableRunner(
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/utils/operator_helpers.py", line 252, in run
    return self.func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/models/baseoperator.py", line 424, in wrapper
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/providers/google/cloud/operators/dataflow.py", line 596, in execute
    self.job = self.hook.start_flex_template(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/providers/google/common/hooks/base_google.py", line 532, in inner_wrapper
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/airflow/providers/google/cloud/hooks/dataflow.py", line 820, in start_flex_template
    response: dict = request.execute(num_retries=self.num_retries)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/googleapiclient/_helpers.py", line 130, in positional_wrapper
    return wrapped(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/python3.11/lib/python3.11/site-packages/googleapiclient/http.py", line 938, in execute
    raise HttpError(resp, content, uri=self.uri)
googleapiclient.errors.HttpError: <HttpError 403 when requesting https://dataflow.googleapis.com/v1b3/projects/gcp-agent-garden/locations/europe-west1/flexTemplates:launch?alt=json returned "(ba5f06a874b0caf6): Current user cannot act as service account 1051082499499-compute@developer.gserviceaccount.com. Enforced by Org Policy constraint constraints/dataflow.enforceComputeDefaultServiceAccountCheck. https://cloud.google.com/iam/docs/service-accounts-actas Causes: (ba5f06a874b0c79e): Current user  cannot act as service account 1051082499499-compute@developer.gserviceaccount.com. If the service account belongs to the current project, please grant your user account one of [Owner, Editor, Service Account User] roles, or any other role that includes the iam.serviceAccounts.actAs permission. See https://cloud.google.com/iam/docs/service-accounts-actas for additional details. If the service account belongs to another project, please disable the iam.disableCrossProjectServiceAccountUsage org-policy constraint on the project the service account belongs to. See https://cloud.google.com/iam/docs/attach-service-accounts#attaching-different-project for additional details.". Details: "(ba5f06a874b0caf6): Current user cannot act as service account 1051082499499-compute@developer.gserviceaccount.com. Enforced by Org Policy constraint constraints/dataflow.enforceComputeDefaultServiceAccountCheck. https://cloud.google.com/iam/docs/service-accounts-actas Causes: (ba5f06a874b0c79e): Current user  cannot act as service account 1051082499499-compute@developer.gserviceaccount.com. If the service account belongs to the current project, please grant your user account one of [Owner, Editor, Service Account User] roles, or any other role that includes the iam.serviceAccounts.actAs permission. See https://cloud.google.com/iam/docs/service-accounts-actas for additional details. If the service account belongs to another project, please disable the iam.disableCrossProjectServiceAccountUsage org-policy constraint on the project the service account belongs to. See https://cloud.google.com/iam/docs/attach-service-accounts#attaching-different-project for additional details.">
[2025-07-10, 09:02:05 UTC] {local_task_job_runner.py:266} INFO - Task exited with return code 1
[2025-07-10, 09:02:05 UTC] {taskinstance.py:3904} INFO - 0 downstream tasks scheduled from follow-on schedule check
[2025-07-10, 09:02:05 UTC] {local_task_job_runner.py:245} ▲▲▲ Log group end


# issue 4


googleapiclient.errors.HttpError: <HttpError 403 when requesting https://dataflow.googleapis.com/v1b3/projects/gcp-agent-garden/locations/europe-west1/flexTemplates:launch?alt=json returned "(9c1a4a338061126c): Current user  cannot act as service account getwellsoon-dataflow-service@gcp-agent-garden.iam.gserviceaccount.com. If the service account belongs to the current project, please grant your user account one of [Owner, Editor, Service Account User] roles, or any other role that includes the iam.serviceAccounts.actAs permission. See https://cloud.google.com/iam/docs/service-accounts-actas for additional details. If the service account belongs to another project, please disable the iam.disableCrossProjectServiceAccountUsage org-policy constraint on the project the service account belongs to. See https://cloud.google.com/iam/docs/attach-service-accounts#attaching-different-project for additional details. Causes: (9c1a4a338061126c): Current user  cannot act as service account getwellsoon-dataflow-service@gcp-agent-garden.iam.gserviceaccount.com. If the service account belongs to the current project, please grant your user account one of [Owner, Editor, Service Account User] roles, or any other role that includes the iam.serviceAccounts.actAs permission. See https://cloud.google.com/iam/docs/service-accounts-actas for additional details. If the service account belongs to another project, please disable the iam.disableCrossProjectServiceAccountUsage org-policy constraint on the project the service account belongs to. See https://cloud.google.com/iam/docs/attach-service-accounts#attaching-different-project for additional details.". Details: "(9c1a4a338061126c): Current user  cannot act as service account getwellsoon-dataflow-service@gcp-agent-garden.iam.gserviceaccount.com. If the service account belongs to the current project, please grant your user account one of [Owner, Editor, Service Account User] roles, or any other role that includes the iam.serviceAccounts.actAs permission. See https://cloud.google.com/iam/docs/service-accounts-actas for additional details. If the service account belongs to another project, please disable the iam.disableCrossProjectServiceAccountUsage org-policy constraint on the project the service account belongs to. See https://cloud.google.com/iam/docs/attach-service-accounts#attaching-different-project for additional details. Causes: (9c1a4a338061126c): Current user  cannot act as service account getwellsoon-dataflow-service@gcp-agent-garden.iam.gserviceaccount.com. If the service account belongs to the current project, please grant your user account one of [Owner, Editor, Service Account User] roles, or any other role that includes the iam.serviceAccounts.actAs permission. See https://cloud.google.com/iam/docs/service-accounts-actas for additional details. If the service account belongs to another project, please disable the iam.disableCrossProjectServiceAccountUsage org-policy constraint on the project the service account belongs to. See https://cloud.google.com/iam/docs/attach-service-accounts#attaching-different-project for additional details.">
[2025-07-10, 09:28:15 UTC] {local_task_job_runner.py:266} INFO - Task exited with return code 1
[2025-07-10, 09:28:15 UTC] {taskinstance.py:3904} INFO - 0 downstream tasks scheduled from follow-on schedule check
[2025-07-10, 09:28:15 UTC] {local_task_job_runner.py:245} ▲▲▲ Log group end

## issue 5

Failed to start the VM, launcher-2025071003550017293866963799895596, used for launching because of status code: INVALID_ARGUMENT, reason: Invalid Error:
 Message: Invalid value for field 'resource.networkInterfaces[0].subnetwork': 'subnetwork=regions/europe-west1/subnetworks/mcd-eu-west1-subnet1'. The URL is malformed.
 HTTP Code: 400.


# issue 6 

e:latest
Step #1:  976d7ac8a19c
Step #1: Step 2/6 : WORKDIR /dataflow/template
Step #1:  Running in dbd9d9b10a23
Step #1: Removing intermediate container dbd9d9b10a23
Step #1:  20706d6f0424
Step #1: Step 3/6 : COPY streaming_pipeline.py .
Step #1:  12913879f0e7
Step #1: Step 4/6 : COPY ../common/masking_utils.py common/masking_utils.py
Step #1: COPY failed: forbidden path outside the build context: ../common/masking_utils.py ()
Finished Step #1
ERROR
ERROR: build step 1 "gcr.io/cloud-builders/docker" failed: step exited with non-zero status: 1
--------------------------------------------------------------------------------

BUILD FAILURE: Build step failure: build step 1 "gcr.io/cloud-builders/docker" failed: step exited with non-zero status: 1
ERROR: (gcloud.builds.submit) build ca9be0b9-4f19-4cfe-bcf1-c40b2c6198ab completed with status "FAILURE"


2025-07-10 19:33:35.338 IST
docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "/opt/google/dataflow/python_template_launcher": stat /opt/google/dataflow/python_template_launcher: no such file or directory: unknown.

# issue 7 


Finished Step #0 - "terraform-apply"
Starting Step #1
Step #1: Already have image (with digest): gcr.io/cloud-builders/docker
Step #1: unable to prepare context: unable to evaluate symlinks in Dockerfile path: lstat /workspace/dataflow/Dockerfile: no such file or directory
Finished Step #1
ERROR
ERROR: build step 1 "gcr.io/cloud-builders/docker" failed: step exited with non-zero status: 1
--------------------------------------------------------------------------------

BUILD FAILURE: Build step failure: build step 1 "gcr.io/cloud-builders/docker" failed: step exited with non-zero status: 1
ERROR: (gcloud.builds.submit) build d2900343-e089-4da1-a8d1-61994517cd3e completed with status "FAILURE"


# issue 8

{
insertId: "1040483747809619142:524425:0:275983"
jsonPayload: {
message: "cloudservice.service: Main process exited, code=exited, status=1/FAILURE"
}
labels: {6}
logName: "projects/gcp-agent-garden/logs/dataflow.googleapis.com%2Flauncher"
receiveTimestamp: "2025-07-10T14:48:10.815590339Z"
resource: {2}
severity: "ERROR"
timestamp: "2025-07-10T14:48:08.873649Z" 

{
insertId: "1040483747809619142:524425:0:277152"
jsonPayload: {
message: "cloudservice.service: Failed with result 'exit-code'."
}
labels: {6}
logName: "projects/gcp-agent-garden/logs/dataflow.googleapis.com%2Flauncher"
receiveTimestamp: "2025-07-10T14:48:20.819412500Z"
resource: {2}
severity: "ERROR"
timestamp: "2025-07-10T14:48:08.940485Z"
}
{
insertId: "1idzz8xc2xy"
labels: {4}
logName: "projects/gcp-agent-garden/logs/dataflow.googleapis.com%2Fjob-message"
receiveTimestamp: "2025-07-10T14:49:53.909569663Z"
resource: {2}
severity: "ERROR"
textPayload: "Error occurred in the launcher container: could not determine py file from env"
timestamp: "2025-07-10T14:49:52.160761384Z"


# issue 9 

Starting Step #3
Step #3: Pulling image: gcr.io/google.com/cloudsdktool/cloud-sdk
Step #3: Using default tag: latest
Step #3: latest: Pulling from google.com/cloudsdktool/cloud-sdk
Step #3: Digest: sha256:99c8977b5214a2c7da1cd0a77910f37bfbc7d8c3737446b886a5c058706c4c7c
Step #3: Status: Downloaded newer image for gcr.io/google.com/cloudsdktool/cloud-sdk:latest
Step #3: gcr.io/google.com/cloudsdktool/cloud-sdk:latest
Step #3: Using bucket: getwellsoon-bucket-demo
Step #3: ERROR: gcloud crashed (ValueError): Invalid template metadata. Parameter helpText field is empty. Parameter: <ParameterMetadata
Step #3:  enumOptions: []
Step #3:  label: 'Input Pub/Sub subscription'
Step #3:  name: 'input_subscription'
Step #3:  parentTriggerValues: []
Step #3:  regexes: []>
Step #3: 
Step #3: If you would like to report this issue, please run the following command:
Step #3:   gcloud feedback
Step #3: 
Step #3: To check gcloud for common problems, please run the following command:
Step #3:   gcloud info --run-diagnostics
Finished Step #3
ERROR
ERROR: build step 3 "gcr.io/google.com/cloudsdktool/cloud-sdk" failed: step exited with non-zero status: 1
--------------------------------------------------------------------------------------------------------------------------------------------------------------

BUILD FAILURE: Build step failure: build step 3 "gcr.io/google.com/cloudsdktool/cloud-sdk" failed: step exited with non-zero status: 1
ERROR: (gcloud.builds.submit) build 8a4bcb02-6eec-4a7c-939c-1e6dd55545f9 completed with status "FAILURE"

