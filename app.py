import boto3
import os

# Create S3 client
s3 = boto3.client('s3')

bucket_name = 'my-test-bucket-12345-qasim'   # Change bucket name (must be globally unique)
file_path = 'test-files/car.jpg'             # Local file path
object_name = 'car.jpg'                      # Name inside S3


# ------------------------------------------------------------
# 1️⃣ Create Bucket
# ------------------------------------------------------------
def create_bucket():
    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
        )
        print("✅ Bucket created successfully!")
    except Exception as e:
        print("⚠️ Bucket exists or error:", e)


# ------------------------------------------------------------
# 2️⃣ Upload File
# ------------------------------------------------------------
def upload_file():
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print("✅ File uploaded successfully!")
    except Exception as e:
        print("⚠️ Upload error:", e)


# ------------------------------------------------------------
# 3️⃣ List Files in Bucket
# ------------------------------------------------------------
def list_files():
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)

        if "Contents" in response:
            print("\n📂 Files in bucket:")
            for obj in response["Contents"]:
                print(" →", obj["Key"])
        else:
            print("📭 Bucket is empty.")
    except Exception as e:
        print("⚠️ List error:", e)


# ------------------------------------------------------------
# 4️⃣ Download File From S3
# ------------------------------------------------------------
def download_file():
    try:
        s3.download_file(bucket_name, object_name, "downloaded-car.jpg")
        print("✅ File downloaded as downloaded-car.jpg!")
    except Exception as e:
        print("⚠️ Download error:", e)


# ------------------------------------------------------------
# 5️⃣ Generate Presigned URL
# ------------------------------------------------------------
def generate_presigned_url():
    try:
        url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=300  # 5 minutes
        )
        print("\n🔗 Presigned URL:")
        print(url)
    except Exception as e:
        print("⚠️ URL generation error:", e)


# ------------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------------
if __name__ == "__main__":
    print("\n🚀 --- AWS S3 Mini Project Started ---\n")

    create_bucket()
    upload_file()
    list_files()
    download_file()
    generate_presigned_url()

    print("\n🎉 --- Project Completed Successfully ---")
