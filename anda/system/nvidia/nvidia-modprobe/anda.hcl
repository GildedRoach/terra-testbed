project "pkg" {
    rpm {
        spec = "nvidia-modprobe.spec"
    }
    labels = {
        subrepo = "nvidia"
        weekly = 1
    }
}
