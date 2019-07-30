# Load Source Data
import os
from os import listdir
from os.path import isfile, join

import inspect

from app.data.entities import get_data_entity_class
from app.extract.fixedwidth.parsers import FixedWidthParser
from app.utilities import (
    get_data_entity_type,
    get_file_type,
    to_bytes,
)
from app.utilities.enums import (
    EtlFileTypes,
)

# Create List of Files in the source_data_type directory

# Initiaize filepath

sourcedata_path = os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))), 'source_data')

sourcedata_files = [f for f in listdir(sourcedata_path) if isfile(join(sourcedata_path, f))]
print(sourcedata_files)


# Check the source data file type
# .txt = fixed width
# .csv = CSV delimited

# Run File Import

for sourcedata_file in sourcedata_files:

    etl_data_entity_type = get_data_entity_type(sourcedata_file)
    etl_file_type = get_file_type(sourcedata_file)
    print("\n'{}' is a '{}' file of '{}' records".format(sourcedata_file, etl_file_type, etl_data_entity_type))

    sourcedata_filepath = '{}/{}'.format(sourcedata_path, sourcedata_file)

    if etl_file_type == EtlFileTypes.TXT.value:
        print("Instantiate a FixedWidthParser")
        data_parser = FixedWidthParser(source_data_type=etl_data_entity_type)

    else:
        print("There is no existing support for importing a {} file".format(etl_file_type))
        continue

    print("Open file '{}'\n".format(sourcedata_filepath))

    with open(sourcedata_filepath, 'r') as f:
        n = 1

        transformed_data_entity = get_data_entity_class(etl_data_entity_type=etl_data_entity_type)

        target_data_entity = list()

        for line in f:
            try:
                # parse the line of data
                parsed_data = data_parser.parse_textdata(to_bytes(line))
            except Exception as e:
                print("problem with line #{}".format(n))
                print(line)
                print(e)
                break

            try:
                # load it into the Data Entity class
                parsed_record = transformed_data_entity(*parsed_data)
            except Exception as e:
                print("problem with line #{}".format(n))
                print(line)
                print(e)
                break

            try:
                # Load data into target
                target_data_entity.append(parsed_record)

            except Exception as e:
                print("problem with line #{}".format(n))
                print(line)
                print(e)
                break

            n += 1

        print("'target_data_entity' is:")
        print(target_data_entity)

print("\n")
