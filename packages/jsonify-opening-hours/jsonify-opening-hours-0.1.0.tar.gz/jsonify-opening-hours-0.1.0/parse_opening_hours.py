# parse various types of strings representing opening hours for a business into machine-readable JSON
# parse into the following format:
#  [
#     {
#       day: str as lowercase day of week e.g. monday,
#       opens: str as time with facility opens on this day in format hh:mm,
#       closes: str as time with facility closes on this day in format hh:mm,
#     },
#     ...
#   ]

from pyparsing import Word, alphas, nums, oneOf, Optional, Or, OneOrMore, Char
from patterns import *
from helpers import detect_if_pm, str_to_day, day_to_str, expand_day_range, value_from_parsed, str_from_parsed
from models.time import Time, TimeType


class JsonOpeningHours():

	@classmethod
	def parse(self, hours_string, assume_type=None):

		opening_hours_format = Or([
			OneOrMore(daterange + timerange + notes),
			OneOrMore(timerange + daterange + notes)
		])	
		parsed = opening_hours_format.parseString(hours_string)
		opening_hours_json = convert_to_dict(parsed, assume_type=assume_type)


		return opening_hours_json



def create_entry(day, opening, closing, notes=None):
	entry = {
		"day": day,
		"opens": opening,
		"closes": closing
	}
	if notes:
		entry["notes"] = notes
	return entry


def parse_times(result, assume_type=None):
	# assumes that all three (hours, minutes, am_pm) are the same length
	start = value_from_parsed(result, "starttime")
	end = value_from_parsed(result, "endtime")
	start = Time.from_string("".join(start), assume_type=assume_type)
	end = Time.from_string("".join(end), assume_type=assume_type)

	if start.is_am() and end.is_am() and start.get_hours() > end.get_hours():
		end.set_type(TimeType.PM)


	return (
		start.get_as_military_time().to_string(),
		end.get_as_military_time().to_string()
		)

def convert_to_dict(result, assume_type=None):

	opening_hours_json = []

	start_day = str_to_day(str_from_parsed(result, "startday"))
	end_day = str_from_parsed(result, "endday", default=None)
	end_day = str_to_day(end_day[0]) if end_day is not None else end_day
	start_time, end_time = parse_times(result, assume_type=assume_type)
	days = expand_day_range(start_day, end_day)

	for day in days:
		opening_hours_json.append(
			create_entry(
				day_to_str(day),
				start_time,
				end_time
			)
		)

	return opening_hours_json
