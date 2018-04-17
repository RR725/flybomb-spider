
exports.stock = new db.Schema({

	_id: { type: String, required: true },
	stockId: { type: Number, default: 0 }
});
