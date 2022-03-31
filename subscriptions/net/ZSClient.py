import sys


class ZSClient:
    HOST = 'subscriptions.zoho.com'
    CHARSET = "UTF-8"
    VERSION = "v1"
    UserAgentName = "ZohoSubscriptions-Python-Client"
    DefaultAcceptHeader = "application/json"
    oauth_token = None
    organization_id = None

    @staticmethod
    def set_organization_id( organization_id):
        ZSClient.organization_id = organization_id

    @staticmethod
    def set_host(host):
        ZSClient.HOST = host

    @staticmethod
    def set_version(version):
        ZSClient.VERSION = version

    @staticmethod
    def set_oathtoken(oauthtoken):
        if oauthtoken is None or oauthtoken.strip() == "":
            raise sys.exit("OauthToken to speak with Zoho Subscriptions is not set. Please set the oauthtoken in "
                            "System property")
        ZSClient.oauth_token = oauthtoken

    @staticmethod
    def set_user_agent_name(userAgentName):
        ZSClient.UserAgentName = userAgentName

    @staticmethod
    def get_organization_id():
        return ZSClient.organization_id

    @staticmethod
    def get_host():
        return ZSClient.HOST

    @staticmethod
    def get_version():
        return ZSClient.VERSION

    @staticmethod
    def get_Base_url():
        return "https://" + ZSClient.get_host() + "/api/" + ZSClient.get_version()

    @staticmethod
    def get_oauthtoken():
        if ZSClient.oauth_token is None or ZSClient.oauth_token.strip() == "":
            raise Exception(
                "OauthToken to speak with Zoho Subscriptions is not set. Please set the oauthtoken in System property")
        return ZSClient.oauth_token

    @staticmethod
    def get_user_agent_name():
        return ZSClient.UserAgentName