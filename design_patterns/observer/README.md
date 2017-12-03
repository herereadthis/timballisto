# Observer Pattern

The observer pattern is used for one-to-many relationships between objects.

* Multiple *observers* register with a *subject*, waiting to receive a notification that there is a state change.
* The subject provides the interface for observers to register and unregister.
* The subject knows who its observers are.
* Multiple observers can register to the same subject.
* The subject sends the notifications.
* When the subject sends the notification, it only tells the observers that there is a state change. It does not send the state information.
* Once the observers receive the notification, they call the subject to get the new state information.

## Is observer patern the same as "Publisher-Subscriber" (pub-sub) pattern?

* In a pub-sub pattern, the publisher and the subscriber don't know about each other.
* There is **Broker** or **Message Broker** or **Event Bus** that both the publishers and subscribers know about. The broker takes the incoming messages from the publisher and sends them out accordingly.
  * There are several methods for filtering methods, such as topic-based and content-based
* In an observer pattern, the observers are aware of the subject, and the subject has a record of the observers.
* In a pub-sub pattern, the publishers and subscribers don't need to know about each other. They are loosely coupled.