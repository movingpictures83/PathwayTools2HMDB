#allows the remote access to pathway-tools on castalia
import pythoncyc.config as config
import pythoncyc
from pythoncyc.PToolsFrame import PFrame

class PathwayTools2HMDBPlugin:
   def input(self, inputfile):
      params = open(inputfile, 'r')
      self.parameters = dict()
      for line in params:
         contents = line.strip().split('\t')
         self.parameters[contents[0]] = contents[1]
      hostname = self.parameters['hostname']
      config.set_host_name(hostname)

   def run(self):
      pass

   def output(self, outputfile):
      #this creates PGDB object associated with meta(MetaCyc)
      meta = pythoncyc.select_organism('meta')
      #prints pathways of compound specified
      #print meta.pathways_of_compound('1,2-dilinoleoyl-sn-glycero-3-phosphocholine')
      #print meta.pathways_of_compound('sucrose')

      mapping = dict()
      for pway in meta.all_pathways():
         print("PATHWAY: ", pway)
         compounds = meta.compounds_of_pathway(pway)
         for compound in compounds:
            if (compound not in mapping):
               myframe = PFrame(compound, meta, getFrameData=True)
               #print(myframe.__dict__)
               #print('|HMDB|' in myframe.__dict__['dblinks'])
               #x = input()
               if ('dblinks' in myframe.__dict__ and '|HMDB|' in myframe.__dict__['dblinks']):
                  mapping[compound] = myframe.__dict__['dblinks']['|HMDB|'][0]

      print("WRITING FILE...")
      outfile = open(outputfile, 'w')
      for compound in mapping.keys():
         outfile.write(compound+"\t"+mapping[compound]+"\n")

#print PFrame('CPD-9816', meta, getFrameData=True).__dict__
#print PFrame('CPD-9816', meta, getFrameData=True).__dict__['dblinks']
#print PFrame('AMMONIA', meta, getFrameData=True).__dict__['dblinks']['|HMDB|'][0]
#print PFrame('solanapyrone-E', meta, getFrameData=True).__dict__['dblinks']['|HMDB|'][0]
#print PFrame('solanapyrone-E', meta, getFrameData=True).__dict__.keys()#['dblinks']['|HMDB|'][0]
#print PFrame('L-1-GLYCERO-PHOSPHORYLCHOLINE', meta, getFrameData=True).__dict__
#print meta.reactions_of_compound('CPD-19247')

#print PFrame('Compounds', meta, getFrameData=True).__dict__
#print dir(PFrame('Compounds', meta, getFrameData=True).__dict__['pgdb'])
#print PFrame('Compounds', meta, getFrameData=True).__dict__['pgdb']['compounds'].__dict__
#print dir(PFrame('Compounds', meta, getFrameData=True))
#print PFrame('Compounds', meta, getFrameData=True).names
