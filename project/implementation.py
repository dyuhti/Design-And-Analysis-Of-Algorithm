class FraudDetector:
    def __init__(self, amount_threshold, time_threshold, location_threshold, frequency_threshold):
        self.amount_threshold = amount_threshold
        self.time_threshold = time_threshold
        self.location_threshold = location_threshold
        self.frequency_threshold = frequency_threshold
        self.previous_transactions = []

    def flag_transaction(self, transaction):
        flagged = False

        # Rule 1: Unusually large transaction
        if transaction['amount'] > self.amount_threshold:
            flagged = True

        # Rule 2: Multiple locations in a short time
        if len(self.previous_transactions) > 0:
            last_transaction = self.previous_transactions[-1]
            if transaction['location'] != last_transaction['location']:
                time_diff = transaction['timestamp'] - last_transaction['timestamp']
                if time_diff < self.time_threshold:
                    flagged = True

        # Rule 3: High frequency of transactions in a short time
        recent_transactions = [t for t in self.previous_transactions if (transaction['timestamp'] - t['timestamp']) < self.time_threshold]
        if len(recent_transactions) > self.frequency_threshold:
            flagged = True

        self.previous_transactions.append(transaction)
        return flagged

# Example usage
transactions = [
    {'amount': 5000, 'location': 'NY', 'timestamp': 1},
    {'amount': 6000, 'location': 'LA', 'timestamp': 2},
    {'amount': 100, 'location': 'NY', 'timestamp': 3},
    {'amount': 7000, 'location': 'NY', 'timestamp': 4},
    {'amount': 200, 'location': 'NY', 'timestamp': 5},
    {'amount': 8000, 'location': 'TX', 'timestamp': 6},
    {'amount': 900, 'location': 'NY', 'timestamp': 7},
]

detector = FraudDetector(amount_threshold=4000, time_threshold=3600, location_threshold=2, frequency_threshold=2)

flagged_transactions = []
for transaction in transactions:
    if detector.flag_transaction(transaction):
        flagged_transactions.append(transaction)

print("Flagged Transactions:", flagged_transactions)

from sklearn.metrics import precision_score, recall_score, f1_score

true_fraudulent_transactions = [
    {'amount': 5000, 'location': 'NY', 'timestamp': 1},
    {'amount': 6000, 'location': 'LA', 'timestamp': 2},
    {'amount': 7000, 'location': 'NY', 'timestamp': 4},
    {'amount': 8000, 'location': 'TX', 'timestamp': 6}
]

def evaluate_performance(flagged_transactions, true_fraudulent_transactions, transactions):
    y_true = [1 if tx in true_fraudulent_transactions else 0 for tx in transactions]
    y_pred = [1 if tx in flagged_transactions else 0 for tx in transactions]

    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    return precision, recall, f1

precision, recall, f1 = evaluate_performance(flagged_transactions, true_fraudulent_transactions, transactions)

print(f"Precision: {precision}, Recall: {recall}, F1 Score: {f1}")
