def set_options(opt):
  opt.tool_options("compiler_cxx")

def configure(conf):
  conf.check_tool("compiler_cxx")
  conf.check_tool("node_addon")
  libudis86 = conf.check(compiler='cxx', lib='udis86', mandatory=True)

def build(bld):
  obj = bld.new_task_gen("cxx", "shlib", "node_addon")
  obj.cxxflags = ["-g", "-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE", "-Wall", "-ludis86"]
  obj.ldflags = ["-ludis86"]
  obj.target = "udis86_wrap"
  obj.source = "udis86_wrap.cxx"
