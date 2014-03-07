#!/usr/bin/env python3
#
#handler routines for creating and converting data files

import blendomatic
import gamedata.empiresdat
from fnmatch import fnmatch
from util import dbg, set_write_dir, merge_data_dump, transform_dump, file_write, file_get_path


def data_generate(args):

	list_enabled = False
	write_enabled = False

	#write mode is disabled by default, unless output is set
	if args.output != None:
		dbg("setting write dir to " + args.output, 1)
		set_write_dir(args.output)
		write_enabled = True
	else:
		if args.list_files:
			set_write_dir("")
			list_enabled = True


	#these sections of the empiresdat will be exported
	empiresdat_sections = ["terrain"]

	storeas = ["struct", "cfile"]

	struct_dumps = list()
	struct_dumps.append(gamedata.empiresdat.EmpiresDat.structs(empiresdat_sections))
	struct_dumps.append(blendomatic.Blendomatic.structs())

	output_storage = list()
	for struct in struct_dumps:
		output_storage.append(transform_dump(struct, storeas))

	output_filenames = list()

	written_file_count = 0

	for dump in output_storage:
		merged_dump = merge_data_dump(dump)

		for file_name, file_data in merged_dump.items():
			output_filenames.append(file_name)

			if write_enabled:
				#only generate requested files
				write_file = False

				if args.filename == "*":
					write_file = True

				if any((fnmatch(file_name, file_pattern) for file_pattern in args.filename)):
					write_file = True

				if write_file:
					#write dat shit
					dbg("writing %s.." % file_name, 1)
					file_name = file_get_path(file_name, write=True)
					file_write(file_name, file_data)
					written_file_count += 1

	if list_enabled:
		#TODO: maybe implement other output formats...
		print(";".join(output_filenames), end="")

	else:
		if written_file_count == 0:
			dbg("no source files generated!", 0)
