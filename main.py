# coding:utf-8
from wox import Wox, WoxAPI
import sys
import pyperclip

if sys.version[0] == "2":
    reload(sys)
    sys.setdefaultencoding("utf-8")


class Main(Wox):

    def query(self, key):
        results = []

        if not key:
            self._construct_result("请输入", None, results)
            return results

        domain = key.encode("idna").decode()
        if domain != key:
            self._construct_result_with_copy(domain, "回车拷贝", [domain], results)

        try:
            domain = key.encode().decode("idna")
            if domain != key:
                self._construct_result_with_copy(domain, "回车拷贝", [domain], results)
        except:
            pass

        return results

    @classmethod
    def _construct_result(cls, title, subtitle, results):
        results.append({
            "Title": title,
            "SubTitle": subtitle,
            "IcoPath": "images/icon.png",
        })

    @classmethod
    def _construct_result_with_copy(cls, title, subtitle, parameters, results):
        results.append({
            "Title": title,
            "SubTitle": subtitle,
            "IcoPath": "images/icon.png",
            "JsonRPCAction": {
                "method": "copy_to_clip",
                "parameters": parameters,
                "dontHideAfterAction": False
            }
        })

    def copy_to_clip(self, text):
        pyperclip.copy(text)


if __name__ == "__main__":
    Main()
