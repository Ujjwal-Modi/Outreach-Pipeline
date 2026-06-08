import { useState } from "react";
import api from "../services/api";
import StatCard from "../components/StatCard";
import CompanyCard from "../components/CompanyCard";
import ContactCard from "../components/ContactCard";
import ConfirmationModal from "../components/ConfirmationModal";
export default function Dashboard() {
  const [domain, setDomain] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [showModal, setShowModal] = useState(false);
  const [sending, setSending] = useState(false);
  const [success, setSuccess] = useState(false);

  const handlePreview = async () => {
    if (!domain) return;

    try {
      setLoading(true);

      const res = await api.post("/preview", {
        domain,
      });

      setData(res.data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const handleSendEmails = async () => {
    try {
      setSending(true);

      await api.post("/send", {
        contacts: data.contacts,
      });

      setSuccess(true);

      setShowModal(false);
    } catch (error) {
      console.error(error);
    } finally {
      setSending(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white p-8">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-5xl font-bold">Automated Outreach Pipeline</h1>

        <p className="text-slate-400 mt-3">Ocean → Prospeo → Brevo</p>

        <div className="flex gap-3 mt-8">
         <input
  value={domain}
  onChange={(e) => setDomain(e.target.value)}
  onKeyDown={(e) => e.key === "Enter" && handlePreview()}
  placeholder="Enter company domain"
  className="
    flex-1
    bg-slate-900
    border
    border-slate-700
    rounded-xl
    px-4
    py-3
    text-white
    outline-none
    focus:border-violet-500
    focus:ring-2
    focus:ring-violet-500/30
    transition-all
    duration-200
  "
/>
<button
  onClick={handlePreview}
  className="
    px-6
    py-3
    bg-violet-600
    rounded-xl
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
  {loading ? "Loading..." : "Preview"}
</button>
        </div>

        {/* stat card */}
        {data && (
          <div className="grid md:grid-cols-2 gap-4 mt-8">
            <StatCard title="Companies Found" value={data.companies_found} />

            <StatCard title="Contacts Found" value={data.contacts_found} />
          </div>
        )}
        {/* company card */}
        {data && data.companies?.length > 0 && (
          <>
            <h2 className="text-2xl font-bold mt-10 mb-4">Similar Companies</h2>

            <div className="grid md:grid-cols-2 gap-4">
              {data.companies.map((company, index) => (
                <CompanyCard key={index} company={company} />
              ))}
            </div>
          </>
        )}
        {/* contact card */}
        {data && data.contacts?.length > 0 && (
          <>
            <h2 className="text-2xl font-bold mt-10 mb-4">Decision Makers</h2>

            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
              {data.contacts.map((contact, index) => (
                <ContactCard key={index} contact={contact} />
              ))}
            </div>
          </>
        )}
        {/* send button */}
        {data && data.contacts?.length > 0 && (
          <div className="mt-10">
            <button
              onClick={() => setShowModal(true)}
              className="
          px-8
          py-4
          bg-violet-600
          rounded-xl
          text-lg
          font-semibold
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
              Send Outreach Emails
            </button>
          </div>
        )}
        {/* success message */}
        {success && (
          <div
            className="
        mt-4
        p-4
        rounded-xl
        bg-green-900/30
        border
        border-green-700
      "
          >
            ✅ Emails sent successfully
          </div>
        )}
      </div>
      <ConfirmationModal
        isOpen={showModal}
        onClose={() => setShowModal(false)}
        onConfirm={handleSendEmails}
        contactsCount={data?.contacts_found || 0}
        companiesCount={data?.companies_found || 0}
        sending={sending}
      />
    </div>
  );
}
