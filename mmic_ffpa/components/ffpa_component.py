from ..models.input import AssignInput
from ..models.output import AssignOutput
from mmic.components.blueprints import GenericComponent
from qcelemental.util import which_import
import importlib
from typing import Dict, Tuple, List, Optional, Any

__all__ = ["AssignComponent"]


class AssignComponent(GenericComponent):
    @classmethod
    def input(cls):
        return AssignInput

    @classmethod
    def output(cls):
        return AssignOutput

    @property
    def supported_comps(self) -> Dict[str, str]:
        """Returns the supported components e.g. {'eng': 'mmic_eng'}.
        Returns
        -------
        Dict[str, str]
        """
        return {"gmx": "mmic_ffpa_gmx"}

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:

        if isinstance(inputs, self.input()):
            inputs = inputs.dict()

        component = inputs.get("component", self.supported_comps["gmx"])

        if which_import(component):
            mod = importlib.import_module(component)
            inputs["engine"] = mod.engine
            return True, mod.runComponent.compute(inputs)
        else:
            raise ModuleNotFoundError(f"Component {inputs.component} is not installed.")
