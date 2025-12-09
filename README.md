Q1.What Does this Project do ?

Ans:-This is a Python automation project where I used Python and the Boto3 library to interact with AWS S3.
My script performs a complete workflow of creating a bucket, uploading a file, listing the contents, downloading the file, and generating a presigned URL.


Q2.If i want to Delete Everything at Last then what should i do ?

Ans:- Just remove the Existing Code & Use below Conde & Run it

import boto3

# Create S3 client
s3 = boto3.client('s3')

bucket_name = 'my-test-bucket-12345-qasim'
object_name = 'car.jpg'

# ------------------------------------------------------------
# Delete file from bucket
# ------------------------------------------------------------
def delete_file():
    try:
        s3.delete_object(Bucket=bucket_name, Key=object_name)
        print("🗑️ File deleted successfully!")
    except Exception as e:
        print("⚠️ Error deleting file:", e)


# ------------------------------------------------------------
# Delete bucket (bucket must be empty)
# ------------------------------------------------------------
def delete_bucket():
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print("🗑️ Bucket deleted successfully!")
    except Exception as e:
        print("⚠️ Error deleting bucket:", e)


# ------------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------------
if __name__ == "__main__":
    print("\n--- AWS S3 Cleanup Started ---\n")

    delete_file()        # Delete object
    delete_bucket()      # Delete bucket

    print("\n--- Cleanup Complete ---")

