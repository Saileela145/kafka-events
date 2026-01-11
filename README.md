# Kafka Streaming Demo using Redpanda Cloud

This project demonstrates a real-time event streaming system using:
- Redpanda Cloud (Kafka protocol)
- Python Producer
- Python Consumer
- SASL Authentication (SCRAM-SHA-256)

## Architecture

Producer → Kafka (Redpanda Cloud) → Consumer

## Tech Stack

✔ Python  
✔ Kafka API  
✔ Redpanda Cloud  
✔ SASL Authentication  
✔ JSON events  


## How to Run

### 1. Install dependencies

''' pip install -r requirements.txt
'''

### 2. Run Producer

''' python producer/producer.py
'''

### 3. Run Consumer

'''python consumer/consumer.py
'''

## Sample Output

**Producer**

* PS D:\kafka-events\producer> python producer.py
* Produced: {'event_id': 0, 'user': 'user_0', 'action': 'click', 'timestamp': 1768149330.1082757}
* Produced: {'event_id': 1, 'user': 'user_1', 'action': 'click', 'timestamp': 1768149335.42069}
* Produced: {'event_id': 2, 'user': 'user_2', 'action': 'click', 'timestamp': 1768149336.70973}
* Produced: {'event_id': 3, 'user': 'user_3', 'action': 'click', 'timestamp': 1768149339.939994}
* Produced: {'event_id': 4, 'user': 'user_4', 'action': 'click', 'timestamp': 1768149341.381874}
* Produced: {'event_id': 0, 'user': 'user_0', 'action': 'click', 'timestamp': 1768149342.6957202}

**consumer**

* PS D:\kafka-events\consumer> python consumer.py
* Waiting for messages...
* Consumed: {'event_id': 3, 'user': 'user_3', 'action': 'click', 'timestamp': 1768148998.484859}
* Consumed: {'event_id': 0, 'user': 'user_0', 'action': 'click', 'timestamp': 1768149082.5780292}
* Consumed: {'event_id': 4, 'user': 'user_4', 'action': 'click', 'timestamp': 1768149091.6241007}
* Consumed: {'event_id': 0, 'user': 'user_0', 'action': 'click', 'timestamp': 1768148990.196704}
* Consumed: {'event_id': 2, 'user': 'user_2', 'action': 'click', 'timestamp': 1768148997.202975}


