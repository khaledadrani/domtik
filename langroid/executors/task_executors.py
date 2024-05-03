import concurrent.futures
from typing import Callable


def execute_tasks(task: Callable,
                  inputs,
                  executor_entity,
                  post_process_global: Callable = None,
                  post_process_batch: Callable = None,
                  max_workers=10, *args, **kwargs):
    data = []
    try:
        with executor_entity(max_workers=max_workers) as executor:
            # Start the load operations and mark each future with its URL
            future_to_result = {executor.submit(task, input, *args, **kwargs): input for input in inputs}
            # print(future_to_url)
            for future in concurrent.futures.as_completed(future_to_result):
                # print(future)
                url = future_to_result[future]
                try:
                    record = future.result()

                    if post_process_batch:
                        record = post_process_batch(record)

                    data.append(record)
                except Exception as exc:
                    print('a certain context generated an exception: ', exc)

        if post_process_global:
            data = post_process_global(data)

        return data
    except Exception as err:
        print('Global Error!: ', str(err))
        raise err
