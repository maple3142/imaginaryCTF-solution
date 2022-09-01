type Props = {
  content: string;
};

const PostBody = ({ content }: Props) => {
  return (
    <div className="flex">
      <div
        dangerouslySetInnerHTML={{ __html: content }}
        className="prose lg:prose-xl mx-auto"
      ></div>
    </div>
  );
};

export default PostBody;
