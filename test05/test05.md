Here the monitoring uses prometheus and installs node-exporter to all instances as an agent that sends log metrics to prometheus.

![1](https://github.com/asepboy/test-sre-kumparan/blob/main/test05/test05-c.jpg)

Setting up multiple aws instances for required services

![2](https://github.com/asepboy/test-sre-kumparan/blob/main/test05/test05-a.jpg)

Create a prometheus.yml configuration file to implement communication of all services and send node-exporter logs of all instances to prometheus.

![3](https://github.com/asepboy/test-sre-kumparan/blob/main/test05/test05-d.jpg)

The result of all instances that are up means all instances that are connected to node-exporter and send log metrics to monitoring prometheus.

![4](https://github.com/asepboy/test-sre-kumparan/blob/main/test05/test05-b.jpg)
