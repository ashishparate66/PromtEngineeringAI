**Problem 1:**

- **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
- **Problem**: Create a **`Customers`** table / collection with the following fields: **`id`** (unique identifier), **`name`**, **`email`**, **`address`**, and **`phone_number`**.

*Answer 1:* <br>
{<br>
  "_id": ObjectId(),<br>
  "name": String,<br>
  "email": String,<br>
  "address": String,<br>
  "phone_number": String <br>
}

*************************************************************

Problem 2:
- **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
- **Problem**: Insert five rows / documents into the **`Customers`** table / collection with data of your choice.

*Answer 2:* <br>

name:"hari",<br>
email:"hari@gmail.com",<br>
address:"nagpur",<br>
phone_number:"123456"<br>

name:"ram",<br>
email:"ram@gmail.com",<br>
address:"pune",<br>
phone_number:"12357856"<br>

*************************************************************
**Problem 3:**

- **Prerequisite**: Understand basic data fetching in SQL / MongoDB
- **Problem**: Write a query to fetch all data from the **`Customers`** table / collection.

*Answer 3:* <br>

db.Customers.find()
*************************************************************
**Problem 4:**

- **Prerequisite**: Understand how to select specific fields in SQL / MongoDB
- **Problem**: Write a query to select only the **`name`** and **`email`** fields for all customers.

*Answer 4:* <br>

db.Customers.find({},name:1,email:1)

*************************************************************
**Problem 5:**

- **Prerequisite**: Understand basic WHERE clause in SQL / MongoDB's find method
- **Problem**: Write a query to fetch the customer with the **`id`** of 3.

*Answer 5:* <br>

db.Customer.find({_id: 3})
*************************************************************
**Problem 6:**

- **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
- **Problem**: Write a query to fetch all customers whose **`name`** starts with 'A'.

*Answer 6:* <br>
db.Customers.find({name:{$regex: '^A'}})

*************************************************************
**Problem 7:**

- **Prerequisite**: Understand how to order data in SQL / MongoDB
- **Problem**: Write a query to fetch all customers, ordered by **`name`** in descending order.
*Answer 7:* <br>
db.Customers.find().sort({name:-1})
*************************************************************
**Problem 8:**

- **Prerequisite**: Understand data updating in SQL / MongoDB
- **Problem**: Write a query to update the **`address`** of the customer with **`id`** 4.

*Answer 8:* <br>
db.Customers.updateOne({ _id: 4 },{ $set: { address: "New Address" } })
*************************************************************
**Problem 9:**

- **Prerequisite**: Understand how to limit results in SQL / MongoDB
- **Problem**: Write a query to fetch the top 3 customers when ordered by **`id`** in ascending order.

*Answer 9:* <br>
db.Customers.find().sort({_id:1}).limit(3)
*************************************************************

**Problem 10:**

- **Prerequisite**: Understand data deletion in SQL / MongoDB
- **Problem**: Write a query to delete the customer with **`id`** 2.

*Answer 10:* <br>
db.Customers.deleteOne({_id:2})
*************************************************************

**Problem 11:**

- **Prerequisite**: Understand how to count rows / documents in SQL / MongoDB
- **Problem**: Write a query to count the number of customers.

*Answer 11:* <br>
db.Customers.countDocuments()
*************************************************************

**Problem 12:**

- **Prerequisite**: Understand how to skip rows / documents in SQL / MongoDB
- **Problem**: Write a query to fetch all customers except the first two when ordered by **`id`** in ascending order.

*Answer 12:* <br>
db.Customers.find().sort({_id:1}).skip(2)
*************************************************************

**Problem 13:**

- **Prerequisite**: Understand filtering with multiple conditions in SQL / MongoDB
- **Problem**: Write a query to fetch all customers whose **`id`** is greater than 2 and **`name`** starts with 'B'.

*Answer 13:* <br>
db.Customers.find({_id:{$gt:2},{name:{$regex:'^B'}}})
*************************************************************

**Problem 14:**

- **Prerequisite**: Understand how to use OR conditions in SQL / MongoDB
- **Problem**: Write a query to fetch all customers whose **`id`** is less than 3 or **`name`** ends with 's'.

*Answer 14:* <br>
db.Customers.find({$or:[{_id:{$lt:3}},{name:{$regex:/s$/i }]})
*************************************************************

**Problem 15:**

- **Prerequisite**: Understand how to use NULL checks in SQL / MongoDB
- **Problem**: Write a query to fetch all customers where the **`phone_number`** field is not set or is null.

*Answer 15:* <br>
db.Customers.find({$or:[
{phone_number:{$exists:false}},
{phone_number:null}
 ]
})
*************************************************************
