import face_recognition
import pickle
import os 

#your face dataset directory (only for .jpg)
file_dir = "C:/Users/mike/python/labels"

#initialize variables
all_face_encodings = {}
count = 0

for root, dirs, files in os.walk(file_dir):
	for f in files:		
		count = count + 1
		print(f)
		f_name = f.split(".jpg", 1)[0]
		#print(f_name)
		path = os.path.join(root,f)
		image = face_recognition.load_image_file(path)
		face_locations = face_recognition.face_locations(image,number_of_times_to_upsample=2)
		all_face_encodings[f_name] = face_recognition.face_encodings(image,face_locations,num_jitters=10)[0]

#save to the dat file
with open('dataset_faces.dat', 'wb') as f:
	pickle.dump(all_face_encodings, f)

print("total jpgs: " + str(count))