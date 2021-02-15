from typing import Any, Dict, Optional
from mmic_ffpa.components.compute_component import ComputeComponent
from mmic_ffpa.models.output import ComputeOutput
from mmelemental.models.util.output import CmdOutput
import os


class ComputeComponent(ComputeComponent):
    """ A component for generating a pramaterized molecule. """

    def build_input(
        self,
        input_model: Dict[str, Any],
        config: Optional["TaskConfig"] = None,
        template: Optional[str] = None,
    ) -> Dict[str, Any]:

        assert input_model["engine"] == "gmx", "Engine must be GROMACS/gmx!"
        cmd = [input_model["engine"], "pdb2gmx"]

        for key, val in input_model.items():
            if key == "forcefield":
                cmd.extend(["-ff", val])
            if key == "mol":
                cmd.extend(["-f", val])
            if key == "solv_forcefield":
                if val:
                    cmd.extend(["-water", val])
                else:
                    cmd.extend(["-water", "none"])

        env = os.environ.copy()

        if config:
            env["MKL_NUM_THREADS"] = str(config.ncores)
            env["OMP_NUM_THREADS"] = str(config.ncores)

        scratch_directory = config.scratch_directory if config else None

        return {
            "command": cmd,
            "infiles": None,
            "outfiles": ["conf.gro", "topol.top", "posre.itp"],
            "scratch_directory": scratch_directory,
            "environment": env,
            "clean_files": input_model.get("clean_files"),
        }

    def parse_output(
        self, output: Dict[str, str], inputs: Dict[str, Any]
    ) -> ComputeOutput:
        stdout = output["stdout"]
        stderr = output["stderr"]
        outfiles = output["outfiles"]

        if stderr:
            # Supress stderro for now because
            # stupid GMX prints pdb2gmx output to stderr
            # See https://redmine.gromacs.org/issues/2211
            if output.get("Debug"):
                print("Error from {engine}:".format(**inputs))
                print("=========================")
                raise RuntimeError(stderr)

        conf = outfiles["conf.gro"]
        top = outfiles["topol.top"]
        # posre = outfiles['posre.itp']
        cmdout = CmdOutput(stdout=stdout, stderr=stderr)

        return ComputeOutput(cmdout=cmdout, mol=conf, forcefield=top)
