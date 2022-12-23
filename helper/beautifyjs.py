import os
import jsbeautifier

def beautify_js_files(input_dir, output_dir):
    # Make sure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        # Check if the file is a .js file
        if filename.endswith('.js'):
            print("Beautifying: " + filename)
            # Construct the input and output file paths
            input_filename = os.path.join(input_dir, filename)
            output_filename = os.path.join(output_dir, filename)


            infile = open(input_filename,'r')

            # Run jsbeautifier on the input file and save the output to the output file
            try:
                res = jsbeautifier.beautify(infile.read())
            except:
                print("ERROR BEAUTIFYING: " +filename)
            f = open(output_filename,'a')
            f.write(res)

            f.close()
            infile.close()
    print("Beautification complete!")
                

