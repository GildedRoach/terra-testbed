project pkg {
               arches = ["x86_64"]
	rpm {
		spec = "xone-kmod-common.spec"
	}
	labels {
		mock = 1
                nightly = 1
	}
}
