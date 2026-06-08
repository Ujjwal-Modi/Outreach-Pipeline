export default function CompanyCard({ company }) {
  return (
    <div
      className="
        bg-slate-900
        border
        border-slate-800
        rounded-2xl
        p-5
        hover:border-violet-500
        transition
      "
    >
      <h3 className="text-xl font-semibold">{company.name}</h3>

      <a
        href={`https://${company.domain}`}
        target="_blank"
        rel="noreferrer"
        className="
    text-violet-400
    mt-2
    inline-block
    hover:underline
  "
      >
        {company.domain}
      </a>
    </div>
  );
}
