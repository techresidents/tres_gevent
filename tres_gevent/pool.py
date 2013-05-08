import gevent.queue

from trpycore.pool.queue import QueuePool

class GESClientPool(QueuePool):
    """GESClient pool.

    Example usage:
        with pool.get() as es_client:
            users = es_client.index('users', 'user')
            users.status()
    """
    
    def __init__(self, ges_client_factory, size, queue_class=gevent.queue.Queue):
        """GESClientPool constructor.

        Args:
            ges_client_factory: Factory object to create ESClient objects.
            size: Number of objects to include in pool.
            queue_class: Optional Queue class. If not provided, will
                default to gevent.queue.Queue. The specified class must
                have a no-arg constructor and provide a get(block, timeout)
                method.
        """
        self.ges_client_factory = ges_client_factory
        self.size = size
        self.queue_class = queue_class
        super(GESClientPool, self).__init__(
                self.size,
                factory=self.ges_client_factory,
                queue_class=self.queue_class)
