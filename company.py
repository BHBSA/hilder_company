class Company:
    def __init__(self, company_id, city=None, region=None, address=None, company_name=None,
                 company_short_info=None, company_info=None, business=None, company_size=None,
                 development_stage=None, registration_time=None, registered_capital=None,
                 operating_period=None, company_source=None):
        self.city = city  # 城市
        self.region = region  # 区域
        self.address = address  # 地址
        self.company_name = company_name  # 公司名
        self.company_short_info = company_short_info  # 公司简介
        self.company_info = company_info  # 公司介绍
        self.business = business  # 行业
        self.company_size = company_size  # 公司规模
        self.development_stage = development_stage  # 发展阶段
        self.registration_time = registration_time  # 注册时间
        self.registered_capital = registered_capital  # 注册资本
        self.operating_period = operating_period  # 经营期限
        self.development_stage = development_stage  # 经营范围
        self.company_source = company_source  # source
        self.company_id = company_id  # company_id
