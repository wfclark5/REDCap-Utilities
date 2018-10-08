
files = glob.glob("*.csv")

names = []
reader = []
header = []
final = []
data_stack = []



print str(os.getcwd())

for file in files:
	names.append(file[:-4])
	
for i in range(0, len(files)):
	 final_df = pandas.read_csv(files[i]).head(0)
	 final_df = final_df.drop(final_df.filter(like='_INT').columns, 1) 
	 final_df = final_df.drop(final_df.filter(like='_RAW').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='_MM').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='_YYYY').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='projectid').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='studyid').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='environmentName').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='subjectId').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='StudySiteId').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='siteid').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='Site').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='SiteNumber').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='SiteGroup').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='instanceId').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='InstanceName').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='InstanceRepeatNumber').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='folderid').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='Folder').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='FolderSeq').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='TargetDays').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='InstanceName').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='DataPageId').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='DataPageName').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='PageRepeatNumber').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='RecordId').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='SaveTS').columns, 1)
	 final_df = final_df.drop(final_df.filter(like='INVSITE').columns, 1)
	 final_df = final_df.transpose()
	 data_stack.extend(final_df.index.tolist())
	 final_df.to_csv(str(os.getcwd())+'/output/'+ files[i])

df = pandas.DataFrame(data_stack)

df.to_csv(str(os.getcwd())+'/output/final.csv')
