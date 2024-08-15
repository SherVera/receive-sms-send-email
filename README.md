# **📧 Receive SMS and Send to Email Using AWS**

This project sets up a system to receive SMS messages using AWS services. The SMS messages are routed to an SNS topic, which triggers a Lambda function that sends the generated notifications to specified email recipients using Amazon SES.

![alt text](<Send SMS to Email.jpg>)

## **🚀 Setup Instructions**

### **1️⃣ Setting Up SNS (Simple Notification Service)**

#### **🔸 Create an SNS Topic:**
1. Sign in to the [AWS Management Console](https://aws.amazon.com/).
2. Navigate to **SNS** from the Services menu.
3. Click on **Topics** and then **Create topic**.
4. Choose a topic type (Standard or FIFO), enter a name, and configure any additional settings as needed.
5. Click **Create topic**.

#### **🔸 Subscribe Lambda to the SNS Topic:**
1. After creating the topic, click on **Create subscription**.
2. For **Protocol**, select **AWS Lambda**.
3. For **Endpoint**, choose the Lambda function you’ll create in Step 3.
4. Click **Create subscription**.

### **2️⃣ Setting Up AWS End User Messaging SMS**

AWS End User Messaging SMS is a service that allows you to receive SMS messages using dedicated phone numbers and route them to various destinations, including SNS topics.

#### **🔸 Request a Phone Number:**
1. Sign in to the AWS Management Console.
2. Navigate to **AWS End User Messaging SMS** from the Services menu.
3. Request a new phone number (short code or long code) that you will use to receive SMS messages.
4. Configure the phone number settings, such as message limits and country restrictions.

#### **🔸 Enable Two-Way Messaging:**
1. In the AWS End User Messaging SMS console, locate the phone number you just requested.
2. Enable **Two-Way Messaging** by selecting the **Enable two-way message** option.
3. Set the **Destination type** to **SNS**.
4. Select the SNS topic that you created in the previous step.
5. For **Channel role**, choose **Use SNS topic policies**.

### **3️⃣ Setting Up the Lambda Function**

#### **🔸 Create a Lambda Function:**
1. In the AWS Management Console, navigate to **Lambda** under Compute services.
2. Click **Create function**.
3. Choose **Author from scratch**, give your function a name, and choose a runtime (e.g., Python, Node.js).
4. Assign the necessary permissions for SNS access by attaching a role with `AWSLambdaSNSPolicy`.


1. Save and deploy the Lambda function.
2. Ensure environment variables are correctly set up in the AWS Lambda console if required.

### **4️⃣ Testing the Setup**

#### **🔹 Send an SMS:**
1. From a mobile device, send an SMS to the phone number configured in SNS.
2. Ensure the message is routed through AWS End User Messaging.

#### **🔹 Check Email:**
1. The Lambda function should trigger, process the SMS, and send an email to the configured recipient.
2. Check the inbox of the recipient email to confirm the SMS message was received as an email.

---

## **💻 Lambda Email Notification**

### **Description**

This Lambda function is designed to receive messages from Amazon SNS and send them as emails using Amazon SES (Simple Email Service). The function processes incoming SMS messages and forwards them as emails to a specified recipient.

### **📂 Project Structure**

- **`lambda_function.py`**: Contains the core Lambda function code.
- **`.env`**: File for defining environment variables.
- **`.gitignore`**: Specifies files and directories to be ignored by Git, including sensitive files like `.env`.

### **⚙️ Setup**

1. **Clone the repository:**

    ```
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Configure environment variables:**

    Create a `.env` file in the root of the project with the following content, replacing the values with your own configurations:

    ```
    SMTP_SERVER=smtp.gmail.com
    SMTP_PORT=587
    SMTP_USER=your-email@gmail.com
    SMTP_PASSWORD=your-email-password
    SENDER_EMAIL=your-email@gmail.com
    RECIPIENT_EMAIL=recipient-email@example.com
    ```

4. **Deploy to AWS Lambda:**

    Follow the usual steps to package and deploy your Lambda function on AWS. Ensure that environment variables are correctly set up in the AWS Lambda console.
