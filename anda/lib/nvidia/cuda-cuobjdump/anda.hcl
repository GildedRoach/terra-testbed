project pkg {
    rpm {
        spec = "cuda-cuobjdump.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
