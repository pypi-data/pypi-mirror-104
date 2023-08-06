import json
from typing import List, Any
from .. import const


class MYPReader:
    data: dict
    file_name: str

    def __init__(self, file_name: str = const.filename):
        with open(file_name) as f:
            data: dict = json.load(f)
        self.data = data
        self.file_name = file_name

    def write(self) -> None:
        """Write object instance to `myp.json`"""
        with open(self.file_name, 'wt') as f:
            json.dump(self.data, f, indent=4, sort_keys=True)

    def get_data(self, key: str) -> Any:
        """Get data from object"""
        return self.data[key]

    def set_data(self, key: str, value: Any) -> None:
        """Set data to object"""
        self.data[key] = value

    def add_script(self, name: str, command: str, description: str) -> str:
        """Add script to object"""
        self.data["scripts"][name] = {
            "command": command,
            "description": description,
        }
        return self.data["scripts"][name]

    def remove_script(self, name: str) -> str:
        """Remove script from object"""
        return self.data["scripts"].pop(name)

    def add_dependency(self, package_name: List[str], scope: str = "common"):
        """Add dependency to object"""
        self.data["dependencies"][scope].extend(package_name)
        self.data["dependencies"][scope] = list(
            set(self.data["dependencies"][scope]))

    def get_dependencies(self, scope: str = "all") -> List[str]:
        """Get dependencies of object"""
        deps: dict = self.data["dependencies"]
        if scope == "all":
            return list(set(deps["dev"]+deps["prod"]+deps["common"]))
        elif scope == "prod":
            return list(set(deps["prod"]+deps["common"]))
        elif scope == "dev":
            return list(set(deps["dev"]+deps["common"]))

        return []
