export default function ConfirmationModal({
  isOpen,
  onClose,
  onConfirm,
  contactsCount,
  companiesCount,
  sending,
}) {
  if (!isOpen) return null;

  return (
    <div
      className="
        fixed
        inset-0
        bg-black/70
        flex
        items-center
        justify-center
        z-50
      "
    >
      <div
        className="
          bg-slate-900
          border
          border-slate-800
          rounded-2xl
          p-8
          w-full
          max-w-md
        "
      >
        <h2 className="text-2xl font-bold">
          Confirm Campaign
        </h2>

        <p className="text-slate-400 mt-3">
          Review before sending emails.
        </p>

        <div className="mt-6 space-y-3">

          <div className="flex justify-between">
            <span>Companies</span>
            <span>{companiesCount}</span>
          </div>

          <div className="flex justify-between">
            <span>Recipients</span>
            <span>{contactsCount}</span>
          </div>

        </div>

        <div className="flex gap-3 mt-8">

          <button
            onClick={onClose}
            className="
              flex-1
              py-3
              rounded-xl
              bg-slate-800
              cursor-pointer
    hover:bg-slate-500
    hover:scale-105
    active:scale-95
    active:bg-slate-600
    transition-all
    duration-150
    select-none
            "
          >
            Cancel
          </button>

          <button
            onClick={onConfirm}
            disabled={sending}
            className="
              flex-1
              py-3
              rounded-xl
              bg-violet-600
              cursor-pointer
    hover:bg-violet-500
    hover:scale-105
    active:scale-95
    active:bg-violet-700
    transition-all
    duration-150
    select-none
            "
          >
            {sending
              ? "Sending..."
              : "Send Emails"}
          </button>

        </div>

      </div>
    </div>
  );
}