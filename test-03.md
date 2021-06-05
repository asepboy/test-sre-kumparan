ACID stands for Atomicity, Consistency, Isolation, and Durability. Four characteristics that ensure that database transactions are processed reliably. Here I will give an example of the ACID method on the printer process.

Atomicity refers to the ability of the database to guarantee that all parts of the transaction are executed or not at all. If one part of the transaction fails, the whole transaction fails. Example : 
The whole document is printed or not at all

Consistency ensures data can be returned to the state before the transaction was initiated, in case of failure. Example:
At the end of the transaction, the paper feed is positioned at the top of the page
    
Isolation ensures that transactions that are still in process and have not been committed (committed) must remain isolated from other transactions. Example :
no two documents mixed up when printing

Durability ensures that the data that has been saved (committed data) is kept by the system as it is, even in the event of a system failure and system restart, the data is available in the correct stage and state. Example :
Printer can guarantee that it is not "printing" with an empty cartridge.