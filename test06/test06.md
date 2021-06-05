There are two ways to discover and monitor all services and instances :

1. Server Side Discovery -> Server side discovery adds a load balancer to divide traffic to several nodes so that when there is an addition or subtraction of nodes, the only thing that needs to be configured is the load balancer and here it can monitor all existing nodes.
One service can have multiple load balancers and one load balancer has multiple nodes to share traffic. The disadvantage of using server side discovery is that it is quite expensive to implement because one service must run 2 or more load balancers/routers.

![1](https://github.com/asepboy/test-sre-kumparan/blob/main/test06/test06-a.png)


2. Client Side Discovery with Service Registry -> Client side discovery is an alternative solution if it does not require hardware investment because it does not require a router/load balancer, but the service must know the IP location of all services by asking the service registery. The service registry is a place to store information related to the location of the service. The service registry has a useful feature, namely a health check which will continue to monitor the condition of the node, if a node dies, it will not be forwarded to the intended service.

![2](https://github.com/asepboy/test-sre-kumparan/blob/main/test06/test06-b.png)
