from pytpp.attributes._helper import PropertyMeta
from pytpp.attributes.report_base import ReportBaseAttributes
from pytpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportSshTrendsReportAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=PropertyMeta):
	pass